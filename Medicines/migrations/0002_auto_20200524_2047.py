# Generated by Django 3.0.6 on 2020-05-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='Exp_date',
            field=models.DateField(blank=True),
        ),
    ]
