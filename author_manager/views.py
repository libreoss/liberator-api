from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def author_login(request):
    if request.method == "GET":
        return render(request, "login.html", {})
    else:
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("article_list")
        return redirect("/login/")


@login_required
def author_logout(request):
    logout(request)
    return redirect("article_list")
