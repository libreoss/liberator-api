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
    for a in parsed_articles:
        if a.getTitle().strip() != "":
            entry = Article()
            entry.name = a.getTitle()
            entry.author = a.getAuthor()
            entry.contents_lat = a.getText() # TODO parse only contents without title, author and status, decide cyr vs lat
            entry.source = a.getId()
            dokuwiki_articles.append(entry)


    context = { 'dokuwiki_articles' : dokuwiki_articles,
                'stored_articles' : stored_articles,
                }
    return render(request, 'articles_list.html', context)
