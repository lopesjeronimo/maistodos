import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from credit_card_app.models import CreditCard


# Create your tests here.
class CreditCardModelTests(TestCase):
    def setUp(self) -> None:
        self.credit_card = CreditCard(holder="Fulano", number="4539578763621486", exp_date=datetime.date(2023, 12, 31))

    def test_valid_credit_card(self):
        self.credit_card.full_clean()
        self.credit_card.save()

    def test_invalid_holder(self):
        self.credit_card.holder = "A"
        with self.assertRaises(ValidationError):
            self.credit_card.full_clean()

    def test_invalid_number(self):
        self.credit_card.number = "0000000000000001"
        with self.assertRaises(ValidationError):
            self.credit_card.full_clean()

    def test_valid_cvv(self):
        self.credit_card.cvv = "111"
        self.credit_card.full_clean()
        self.credit_card.save()

    def test_invalid_cvv(self):
        self.credit_card.cvv = "11"
        with self.assertRaises(ValidationError):
            self.credit_card.full_clean()
            self.credit_card.save()
