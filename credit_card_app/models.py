from django.db import models

# Create your models here.


class CreditCard(models.Model):
    exp_date = models.DateField()
    holder = models.CharField(max_length=255)
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4, null=True)
