from django.shortcuts import render
from django.http import HttpResponse
from article_manager.models import Article
from article_manager.forms import ArticleForm

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
            found = False 
            for e in dokuwiki_articles:
                if a.getTitle() == e.name:
                    found = True
            if not found:
                entry = Article()
                entry.name = a.getTitle()
                entry.author = a.getAuthor()
                entry.contents_lat = a.getLatText()
                entry.contents_cyr = ""
                entry.source = a.getId()
                dokuwiki_articles.append(entry)
    not_updated = [] # This is list for placing articles which have not been imported yet
    for dokuwiki_article in dokuwiki_articles:
        if not Article.objects.filter(source = dokuwiki_article.source).exists():
            not_updated.append(dokuwiki_article)
    context = { 'dokuwiki_articles' : not_updated,
                'stored_articles' : stored_articles,
                }
    return render(request, 'articles_list.html', context)

def article_view(request, article_id):
    article = Article.objects.get(pk=int(article_id))
    context = {"article": article}
    return render(request, "article_view.html", context)

def wiki_import(request, wiki_slug):
    imported = 0
    print("slug: " + wiki_slug)

    
    if request.method == "GET":
        remote = LibreManager(settings.DOKUWIKI_USERNAME, settings.DOKUWIKI_PASSWORD)
        parsed_article = remote.getPage(wiki_slug)
        title = parsed_article.getTitle()
        slug = wiki_slug 
        author = parsed_article.getAuthor()
        lat = parsed_article.getLatText()
        cyr = ""
        if parsed_article.isCyr():
            cyr = parsed_article.getText()
        entry = Article()
        entry.name = title 
        entry.author = author
        entry.source = slug
        entry.contents_lat = lat
        entry.contents_cyr = cyr
        form = ArticleForm(instance=entry)
        #c["article_title"] = title
        #c["article_slug"] = slug
        #c["article_author"] = author
        #c["article_lat"] = lat.replace("\n", "&#10;")
        #c["article_cyr"] = cyr.replace("\n", "&#10;")
        return render(request, "wiki_pre_import.html", {"form": form})
    
    form = ArticleForm(request.POST)
    new = form.save(commit=False)
    title = new.name
    slug = new.source
    author = new.author 
    lat = new.contents_lat
    cyr = new.contents_cyr
    if not Article.objects.filter(source = wiki_slug).exists():
        if cyr != "":
                if Article.objects.filter(name = title).exists():
                        entry = Article.objects.get(name = title) 
                        entry.name = title
                        entry.author = author 
                        entry.source = slug 
                        entry.contents_lat = lat
                        entry.contents_cyr = cyr
                        entry.save()
                else: 
                        entry = Article()
                        entry.name = title
                        entry.author = author 
                        entry.source = slug 
                        entry.contents_lat = lat
                        entry.contents_cyr = cyr
                        entry.save()
                imported += 1 # increase number of imported articles in this view
        else:
                try: 
                        entry = Article.get(name = title)
                except ObjectDoesNotExist:
                        entry = Article()
                        entry.name = title
                        entry.author = author 
                        entry.source = slug
                        entry.contents_lat = lat
                        entry.contents_cyr = cyr
                        entry.save()
                        imported += 1 
        
        
    return render(request, "wiki_import.html", {"imported": imported, "wiki_slug": wiki_slug})
