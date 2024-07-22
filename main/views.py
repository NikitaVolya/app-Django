from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели",
        "categories": categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        "title": "about - O нас",
        "content": "Информация",
        "text_on_page": "jaslk;djlas[dajksd[askdja[skdja[sdjasdk[jasjdk[]]]]]]"
    }
    return render(request, "main/about.html", context)
