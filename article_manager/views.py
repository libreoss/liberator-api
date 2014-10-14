from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def article_manager_base_view(request):
    return HttpResponse("Hello there!")
