from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as Author
from django.shortcuts import render

from article_manager.models import Article


@login_required
def article_submit(request, article_id="", script=""):
    if article_id != "":
        if request.method == "GET":
            return render(
                request,
                "editor.html",
                {
                    "article": Article.objects.get(
                        pk=int(article_id)),
                    "script": script
                }
            )
        else:
            document = request.POST["myDoc"]
            title = request.POST["articleTitle"]
            author = request.POST["articleAuthor"]
            stage = request.POST["articleStage"]
            entry = Article.objects.get(pk=article_id)
            entry.name = title
            if script == "cyr":
                entry.contents_cyr = document
            else:
                entry.contents_lat = document
            entry.author = Author.objects.get(username=author)
            entry.stage = stage
            entry.save()
            return render(request, "show_document.html", {"doc": document})
    else:
        if request.method == "GET":
            return render(request, "editor.html", {})
        else:
            document = request.POST["myDoc"]
            title = request.POST["articleTitle"]
            author = request.POST["articleAuthor"]
            stage = request.POST["articleStage"]
            script = request.POST["articleScript"]
            # Check are title and authors fields populated
            if author.strip() and title.strip():
                entry = Article()
                entry.name = title
                entry.author = Author.objects.get(username=author)
                entry.stage = stage
                if script == "lat":
                    entry.contents_lat = document
                else:
                    entry.contents_cyr = document
                entry.save()
            return render(request, "show_document.html", {"doc": document})
