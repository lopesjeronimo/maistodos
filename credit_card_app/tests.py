import datetime
from collections import OrderedDict

import freezegun
import rest_framework.exceptions
from django.core.exceptions import ValidationError
from django.test import TestCase
from rest_framework.test import APITestCase

from credit_card_app.models import CreditCard
from credit_card_app.serializers import CreditCardSerializer


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

    def test_brand(self):
        self.assertEquals(self.credit_card.brand, "visa")


class CreditCardSerializerTests(TestCase):
    @freezegun.freeze_time("2023-08-05")
    def test_valid_payload(self):
        payload = {"holder": "Fulano", "number": "4539578763621486", "exp_date": "06/2030"}

        credit_card_serializer = CreditCardSerializer(data=payload)
        self.assertTrue(credit_card_serializer.is_valid(raise_exception=True))
        credit_card_serializer.save()

        credit_card: CreditCard = CreditCard.objects.last()
        self.assertEquals(credit_card.exp_date, datetime.date(2030, 6, 30))
        self.assertEquals(credit_card.brand, "visa")

    @freezegun.freeze_time("2023-08-05")
    def test_invalid_exp_date(self):
        payload = {"holder": "Fulano", "number": "4539578763621486", "exp_date": "2023-07"}
        credit_card_serializer = CreditCardSerializer(data=payload)

        with self.assertRaises(rest_framework.exceptions.ValidationError):
            credit_card_serializer.is_valid(raise_exception=True)

    @freezegun.freeze_time("2023-08-05")
    def test_past_exp_date(self):
        payload = {"holder": "Fulano", "number": "4539578763621486", "exp_date": "07/2023"}
        credit_card_serializer = CreditCardSerializer(data=payload)

        with self.assertRaises(rest_framework.exceptions.ValidationError):
            credit_card_serializer.is_valid(raise_exception=True)


class CreditCardAPITests(APITestCase):
    def test_list(self):
        credit_card = CreditCard(holder="Fulano", number="4539578763621486", exp_date=datetime.date(2023, 12, 31))
        credit_card.save()
        response = self.client.get("/api/v1/credit-card/")
        self.assertEquals(response.status_code, 200)
