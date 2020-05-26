from django.shortcuts import render


def index(request):
    data = {'title': 'emergency code'}
    return render(request, 'Emergency/index.html', context=data)


def about(request):
    data = {'title': 'about emergency'}
    return render(request, 'Emergency/about.html', context=data)


def contacts(request):
    data = {'title': 'contact emergency services'}
    return render(request, 'Emergency/contacts.html', context=data)


