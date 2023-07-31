import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from credit_card_app.models import CreditCard


# Create your tests here.
class CreditCardModelTests(TestCase):
    def setUp(self) -> None:
        self.valid_credit_card = CreditCard(
            holder="Fulano", number="4539578763621486", exp_date=datetime.date(2023, 12, 31), cvv="123"
        )

    def test_valid_credit_card(self):
        self.valid_credit_card.full_clean()

    def test_invalid_holder(self):
        self.valid_credit_card.holder = "A"
        with self.assertRaises(ValidationError):
            self.valid_credit_card.full_clean()

    def test_invalid_number(self):
        self.valid_credit_card.number = "0000000000000001"
        with self.assertRaises(ValidationError):
            self.valid_credit_card.full_clean()
