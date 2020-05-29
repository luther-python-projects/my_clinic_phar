from django.shortcuts import render, redirect
from .forms import MedicineForm, MedicineForm2
from .models import Medicine


def index(request):
    data = dict()
    data['user'] = "admin"
    data['title'] = 'check medicines'
    data['medicines'] = Medicine.objects.all()
    return render(request, 'Medicines/index.html', context=data)


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


def details(request, medicine_id):
    data = dict()
    data['title'] = 'See details'
    data['medicine'] = Medicine.objects.get(id=medicine_id)
    return render(request, 'Medicines/details.html', context=data)


def edit(request, medicine_id):
    data = dict()
    data['title'] = 'Edit Medicine'
    medicine = Medicine.objects.get(id=medicine_id)
    # del ... ?
    if request.method == 'GET':
        data['form'] = MedicineForm2(instance=medicine)
        data['post'] = medicine
        return render(request, 'Medicines/edit.html', context=data)
    elif request.method == 'POST':
        form2 = MedicineForm2(request.POST)
        if form2.is_valid():
            medicine.description = form2.cleaned_data['description']
            medicine.package = form2.cleaned_data['package']
            medicine.Qte = form2.cleaned_data['Qte']
            medicine.Unit_Price = form2.cleaned_data['Unit_Price']
            medicine.Exp_date = form2.cleaned_data['Exp_date']
            medicine.save()
            # update ?
        return redirect('/Medicines')


def delete(request, medicine_id):
    data = dict()
    data['title'] = 'Delete medicine'
    medicine = Medicine.objects.get(id=medicine_id)
    if request.method == 'GET':
        data['medicine'] = medicine
        return render(request, 'Medicines/delete.html', context=data)
    elif request.method == 'POST':
        medicine.delete()
        return redirect('/Medicines')




