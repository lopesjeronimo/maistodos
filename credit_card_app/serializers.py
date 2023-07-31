import calendar

from rest_framework import serializers

from credit_card_app.models import CreditCard


class ExpirationDateField(serializers.DateField):

    def __init__(self, *args, **kwargs):
        super().__init__(input_formats=['%m/%Y'], *args, **kwargs)

    def to_internal_value(self, value):
        date_value = super().to_internal_value(value)
        weekday, monthday = calendar.monthrange(date_value.year, date_value.month)
        return date_value.replace(day=monthday)


class CreditCardSerializer(serializers.ModelSerializer):

    exp_date = ExpirationDateField()

    class Meta:
        model = CreditCard
        fields = '__all__'
