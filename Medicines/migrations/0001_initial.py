# Generated by Django 3.0.6 on 2020-05-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=100, unique=True)),
                ('package', models.CharField(max_length=30)),
                ('Qte', models.IntegerField()),
                ('Unit_Price', models.FloatField()),
                ('Total', models.FloatField()),
                ('Exp_date', models.DateField()),
            ],
        ),
    ]
