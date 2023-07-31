import calendar
import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from credit_card_app.models import CreditCard


def future_date_validator(value: datetime.date):
    if datetime.date.today() > value:
        raise ValidationError()


class ExpirationDateField(serializers.DateField):
    def __init__(self, **kwargs):
        super().__init__(format="%m/%Y", input_formats=["%m/%Y"], validators=[future_date_validator], **kwargs)

    def to_internal_value(self, value):
        date_value = super().to_internal_value(value)
        weekday, monthday = calendar.monthrange(date_value.year, date_value.month)
        return date_value.replace(day=monthday)


class CreditCardSerializer(serializers.ModelSerializer):
    exp_date = ExpirationDateField()
    brand = serializers.CharField(read_only=True)
    number = serializers.CharField()

    class Meta:
        model = CreditCard
        fields = ["exp_date", "holder", "number", "cvv", "brand", "id"]
