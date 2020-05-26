from django.shortcuts import render


def index(request):
    data = {'title': 'check doctors'}
    return render(request, 'Doctors/index.html', context=data)


def details(request):
    data = {'title': 'see doctor CV'}
    return render(request, 'Doctors/details.html', context=data)


def create(request):
    data = {'title': 'add a doctor to DB'}
    return render(request, 'Doctors/create.html', context=data)


def edit(request):
    data = {'title': ' edit a new doctor'}
    return render(request, 'Doctors/edit.html', context=data)


def delete(request):
    data = {'title': 'delete a doctor'}
    return render(request, 'Doctors/delete.html', context=data)


def update(request):
    data = {'title': 'update a doctor'}
    return render(request, 'Doctors/update.html', context=data)
