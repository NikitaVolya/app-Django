from typing import Mapping
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": "Home",
        "content": "1",
        'a': False
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("About page") 
