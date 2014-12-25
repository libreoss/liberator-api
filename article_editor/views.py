from django.shortcuts import render

from article_manager.models import Article

def article_submit(request, article_id="", script=""):
    if article_id != "": 
        if request.method == "GET":
            return render(request, "editor.html", {"article": Article.objects.get(pk=int(article_id)), "script": script})
        else: 
            document = request.POST["myDoc"]
            title = request.POST["articleTitle"]
            entry = Article(pk = int(article_id))
            entry.name = title
            if script == "cyr": 
                entry.contents_cyr = document 
            else: 
                entry.contents_lat = document
            entry.save()
            return render(request, "show_document.html", {"doc": document})
    else:
        if request.method == "GET":
            return render(request, "editor.html", {})
        else: 
            document = request.POST["myDoc"]
            title = request.POST["articleTitle"]

            entry = Article()
            entry.name = title
            entry.author = "unknown" # Get info about currently logged user
            entry.contents_lat = document 
            entry.save()
            return render(request, "show_document.html", {"doc": document})

