from django.shortcuts import render


def index(request):
    data = {'title': 'Main Menu'}
    return render(request, 'Home/index.html', context=data)


def about(request):
    data = {'title': 'about US'}
    return render(request, 'Home/about.html', context=data)


def contacts(request):
    data = {'title': 'contact US'}
    return render(request, 'Home/contacts.html', context=data)
