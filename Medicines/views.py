from django.shortcuts import render, redirect
from .forms import MedicineForm
from .models import Medicine


def index(request):
    data = dict()
    data['user'] = "admin"
    data['title'] = 'check medicines'
    data['medicines'] = Medicine.objects.all()
    return render(request, 'Medicines/index.html', context=data)


def details(request):
    data = {'title': 'see cure details'}
    return render(request, 'Medicines/details.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'add medicine to DB'
    if request.method == 'GET':
        data['form'] = MedicineForm()
        return render(request, 'Medicines/create.html', context=data)
    elif request.method == 'POST':
        filled_form = MedicineForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/Medicines')


def edit(request):
    data = {'title': ' edit a medicine'}
    return render(request, 'Medicines/edit.html', context=data)


def delete(request):
    data = {'title': 'delete a medicine'}
    return render(request, 'Medicines/delete.html', context=data)


def update(request):
    data = {'title': 'update a medicine'}
    return render(request, 'Medicines/update.html', context=data)
