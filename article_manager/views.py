from django.shortcuts import render, redirect
from django.http import HttpResponse
from article_manager.models import Article, Category
from article_manager.forms import ArticleForm

from article_manager.libre import LibreManager

from django.conf import settings

from difflib import Differ

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def articles_list(request):
    stored_articles = Article.objects.all()
    remote = LibreManager(settings.DOKUWIKI_USERNAME, settings.DOKUWIKI_PASSWORD)

    links = remote.getLocalLinks("wiki:prikupljeni_clanci") # get all available links from dokuwiki

    to_import = [] # This is list for placing articles which have not been imported yet
    for link in links:
        imported = Article.slugInDatabase(link)
        if not imported: imported = Article.slugInDatabase("wiki:" + link) # Try with namespace
        if not imported:
            to_import.append(link)
    context = {
        'dokuwiki_articles' : to_import,
        'stored_articles' : stored_articles,
    }
    return render(request, 'articles_list.html', context)

@login_required
def article_view(request, article_id):
    article = Article.objects.get(pk=int(article_id))
    context = {"article": article}
    return render(request, "article_view.html", context)

@login_required
def article_delete(request, article_id):
    article = Article.objects.get(pk=int(article_id))
    article.delete()
    return redirect("article_list")

@login_required
def article_diff(request, article_id):
    article = Article.objects.get(pk= int(article_id))
    diff = []
    remote = LibreManager(settings.DOKUWIKI_USERNAME, settings.DOKUWIKI_PASSWORD)
    wiki_article = remote.getPage(article.source_lat)
    t1 = []
    t2 = []
    if wiki_article.isCyr():
        t1 = article.contents_cyr.split("\n")
        t2 = wiki_article.getText().split("\n")
    else:
        t1 = article.contents_lat.split("\n")
        t2 = wiki_article.getText().split("\n")
    # We remove blank lines
    nt1 = []
    nt2 = []
    for line in t1:
        if line.strip() != "":
            nt1.append(line.replace("\r", ""))
    for line in t2:
        if line.strip() != "":
            nt2.append(line.replace("\r", ""))
    d = Differ()
    diff = list(d.compare(nt1, nt2))
    context = {"diff": diff}
    return render(request, "article_diff.html", context)

@login_required
def wiki_import(request, wiki_slug, script):
    if request.method == "GET":
        entry = Article.fromRemote(wiki_slug)
        entry.save()
        return redirect("article_submit", entry.pk, script)

@login_required
def wiki_extend(request, wiki_slug, article_id, script):
    wiki = Article.fromRemote(wiki_slug)
    entry = None
    if article_id == "auto":
        entry = wiki.titleInDatabase()
    else:
        entry = Article.objects.get(pk = int(article_id))
    if not entry:
        return redirect("article_list") # TODO redirect to the error message
    if script == "lat":
        entry.contents_lat = wiki.contents_lat
        entry.source_lat = wiki.source_lat
    else:
        entry.contents_cyr = wiki.contents_cyr
        entry.source_cyr = wiki.source_cyr
    entry.save()
    return redirect("article_submit", entry.pk, script)

@login_required
def article_approve(request, article_id):
    if request.method == "GET":
        context = {
            "article": Article.objects.get(pk = int(article_id)),
            "categories": Category.objects.all()
        }
        return render(request, "article_approve.html", context)
    else:
        issue = request.POST["issue"]
        cat = Category.objects.get(pk = request.POST["category"])
        entry = Article.objects.get(pk = article_id)
        entry.approve(cat, issue)
        entry.save()
        return redirect("article_view", article_id)
