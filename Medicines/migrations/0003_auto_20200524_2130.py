# Generated by Django 3.0.6 on 2020-05-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicines', '0002_auto_20200524_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='Exp_date',
            field=models.DateField(),
        ),
    ]
