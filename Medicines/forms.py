from django import forms
from .models import Medicine


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('image', 'description', 'package', 'Qte', 'Unit_Price', 'Total', 'Exp_date')


class MedicineForm2(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('description', 'package', 'Qte', 'Unit_Price', 'Total', 'Exp_date')

