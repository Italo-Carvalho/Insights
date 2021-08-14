from django.shortcuts import render

def Home(request):
    context = {}
    return render(request, 'home.html', context)
