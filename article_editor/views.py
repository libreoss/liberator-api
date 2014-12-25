from django.shortcuts import render

from article_manager.models import Article

def article_submit(request, article_id="", script=""):
    if request.method == "GET":
        if article_id != "": 
            return render(request, "editor.html", {"article": Article.objects.get(pk=int(article_id)), "script": script})
        return render(request, "editor.html", {})
    else: 
        document = request.POST["myDoc"]
        return render(request, "show_document.html", {"doc": document})

