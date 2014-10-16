from django.shortcuts import render
from django.http import HttpResponse
from article_manager.models import Article

from article_manager.libre import LibreManager

from django.conf import settings

# Create your views here.
def articles_list(request):
    stored_articles = Article.objects.all()

    dokuwiki_articles = []

    remote = LibreManager(settings.DOKUWIKI_USERNAME, settings.DOKUWIKI_PASSWORD)
    parsed_articles = remote.getAllLinked("wiki:prikupljeni_clanci")
    
    # separate cyrilic and latin texts 
    parsed_articles_cyr = [] 
    parsed_articles_lat = [] 
    for parsed_article in parsed_articles:
        if parsed_article.isCyr():
            parsed_articles_cyr.append(parsed_article)
        else:
            parsed_articles_lat.append(parsed_article)
    
    # Add cyrilic texts first
    for a in parsed_articles_cyr:
        if a.getTitle().strip() != "":
            entry = Article()
            entry.name = a.getTitle()
            entry.author = a.getAuthor()
            entry.contents_lat = a.getLatText() # TODO parse only contents without title, author and status, decide cyr vs lat
            entry.contents_cyr = a.getText()
            entry.source = a.getId()
            dokuwiki_articles.append(entry)
    # Now we can process articles from latin set and check whether they already exist
    for a in parsed_articles_lat: 
        if a.getTitle().strip() != "":
            # check whether it exists already as cyrilic article
            # NOTE: In future this will be changed with database check 
            found = False 
            for e in dokuwiki_articles:
                if a.getTitle() == e.name:
                    found = True
            if not found:
                entry = Article()
                entry.name = a.getTitle()
                entry.author = a.getAuthor()
                entry.contents_lat = a.getLatText()
                entry.contents_cyr = "There are no cyrilic version right now."
                entry.source = a.getId()
                dokuwiki_articles.append(entry)

    context = { 'dokuwiki_articles' : dokuwiki_articles,
                'stored_articles' : stored_articles,
                }
    return render(request, 'articles_list.html', context)

def article_view(request, article_id):
    article = Article.get(pk=int(article_id))
    context = {"article": article}
    return render(request, context, "article_view.html")

def wiki_import(request, wiki_slug):
    imported = 0
    print("slug: " + wiki_slug)
    remote = LibreManager(settings.DOKUWIKI_USERNAME, settings.DOKUWIKI_PASSWORD)
    parsed_article = remote.getPage(wiki_slug)
    
    title = parsed_article.getTitle()
    slug = wiki_slug 
    author = parsed_article.getAuthor()
    lat = parsed_article.getLatText()
    cyr = ""
    if parsed_article.isCyr():
        cyr = parsed_article.getText()
    if not Article.objects.filter(source = wiki_slug).exists() and cyr != "": # Check wether article already exists
        # NOTE: This only works for articles with cyrilic version
	# TODO Handle articles without cyrilic versions (it can cause problems with collisions etc...)
	entry = Article()
	entry.name = title
	entry.author = author 
	entry.source = slug 
	entry.contents_lat = lat 
	entry.contents_cyr = cyr
	entry.save()
	imported += 1 # increase number of imported articles in this view
    return render(request, "wiki_import.html", {"imported": imported, "wiki_slug": wiki_slug})
