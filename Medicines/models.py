from django.db import models


class Medicine(models.Model):
    description = models.TextField(max_length=100, unique=True, null=False)
    package = models.CharField(max_length=30, unique=False, null=False)
    Qte = models.IntegerField(null=False)
    Unit_Price = models.FloatField(null=False)
    Total = models.FloatField(null=False)
    Exp_date = models.DateField(null=False, auto_now_add=False, auto_now=False,)
