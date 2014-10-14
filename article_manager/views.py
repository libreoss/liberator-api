from django.shortcuts import render
from django.http import HttpResponse
from article_manager.models import Article

# Create your views here.
def articles_list(request):
    stored_articles = Article.objects.all()

    dokuwiki_articles = [] #TODO: fetch'em all!

    context = { 'dokuwiki_articles' : dokuwiki_articles,
                'stored_articles' : stored_articles,
                }
    return render(request, 'articles_list.html', context)
