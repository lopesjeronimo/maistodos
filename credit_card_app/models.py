import creditcard
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django_cryptography.fields import encrypt

# Create your models here.


def credid_card_number_validator(value):
    cc = creditcard.CreditCard(number=value)
    if not cc.is_valid():
        raise ValidationError(f"{value} is not a valid credit card number")


class CreditCard(models.Model):
    exp_date = models.DateField()
    holder = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    number = encrypt(models.CharField(db_column="number", max_length=16, validators=[credid_card_number_validator]))
    cvv = models.CharField(max_length=4, null=True, blank=True, validators=[MinLengthValidator(3)])
