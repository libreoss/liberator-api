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
