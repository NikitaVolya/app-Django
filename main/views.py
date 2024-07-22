from typing import Mapping
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        "title": "about - O нас",
        "content": "Информация",
        "text_on_page": "jaslk;djlas[dajksd[askdja[skdja[sdjasdk[jasjdk[]]]]]]"
    }
    return render(request, "main/about.html", context)
