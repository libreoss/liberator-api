from django.shortcuts import render

def article_submit(request):
    if request.method == "GET":
        return render(request, "editor.html", {})
    else: 
        document = request.POST["myDoc"]
        return render(request, "show_document.html", {"doc": document})

