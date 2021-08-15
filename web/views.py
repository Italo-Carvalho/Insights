from django.shortcuts import render
from .api import ApiService


def Home(request):
    data = ApiService().getData("x", "x", 1)

    context = {
        "data": data,
    }
    return render(request, "home.html", context)


def NewCard(request):

    context = {}
    return render(request, "new_card.html", context)
