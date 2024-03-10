from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.cashflow.models import (Payee, PayeeLabel,
                                  Payment, Source,
                                  Income)


class PayeeLabelTestCase(TestCase):
    def setUp(self):
        self.payeelabel = PayeeLabel.objects.create(
            name='Test Label')

    def test_label_uniqueness(self):
        with self.assertRaises(Exception):
            PayeeLabel.objects.create(name='Test Label')

    def test_payeelabel_created(self):
        self.assertEqual(PayeeLabel.objects.count(), 1)

    def test_str_method(self):
        self.assertEqual(str(self.payeelabel), 'Test Label')

class PayeeTestCase(TestCase):
    def setUp(self):
        self.payeelabel = PayeeLabel.objects.create(
            name='Test Label')
        self.payee = Payee.objects.create(
            label = self.payeelabel,
            name='Test Payee',
        )
    
    def test_payee_created(self):
        self.assertEqual(Payee.objects.count(), 1)

    def test_str_method(self):
        self.assertEqual(str(self.payee), 'Test Payee-Test Label')

    def test_unique_label_name_combination(self):
        with self.assertRaises(Exception):
            PayeeLabel.objects.create(
                label=self.payeelabel,
                name='Test Payee',
                )

    def test_same_label_different_name(self):
        Payee.objects.create(
                label=self.payeelabel,
                name='Test Payee 1',
                )
        self.assertEqual(Payee.objects.count(), 2)

    def test_same_name_different_label(self):
        newlabel = PayeeLabel.objects.create(name='Test Label 2')
        Payee.objects.create(
                label=newlabel,
                name='Test Payee',
                )
        self.assertEqual(Payee.objects.count(), 2)

class SourceTestCase(TestCase):

    def setUp(self):
        self.source = Source.objects.create(
            source='Test Source',
            summary='Test Summary')

    def test_source_uniqueness(self):
        with self.assertRaises(Exception):
            Source.objects.create(source='Test Source')

    def test_source_created(self):
        self.assertEqual(Source.objects.count(), 1)


    def test_str_method(self):
        self.assertEqual(str(self.source), 'Test Source')

    
class IncomeTestCase(TestCase):
    def setUp(self) -> None:
        self.source = Source.objects.create(source='Test Source')     
        self.income = Income.objects.create(
            source=self.source,
            amount = 1245,            
        )

    def test_income_created(self):
        self.assertEqual(Income.objects.count(), 1)
    
    def test_str_method(self):
        self.assertEqual(str(self.income), 'Test Source - 1245')

    def test_no_negative_amount_can_be_saved(self):
        income = Income.objects.create(
                source=self.source,
                amount = -1245,            
            )
        with self.assertRaises(ValidationError):
            income.clean()
            
class PaymentTestCase(TestCase):
    def setUp(self):
        self.payeelabel = PayeeLabel.objects.create(
            name='Test Label')
        self.payee = Payee.objects.create(
            label = self.payeelabel,
            name='Test Payee',
        )
  
    def test_obj_created(self):
        Payment.objects.create(
            payee=self.payee,
            amount=249
        )
        self.assertEqual(Payment.objects.count(), 1)

    def test_str_method(self):
        payment = Payment.objects.create(
            payee=self.payee,
            amount=249
        )
        created_at = payment.created_at.strftime("%b %d %Y")
        self.assertEqual(str(payment), f'Test Payee - {created_at}')

    def test_no_negative_amount_can_be_saved(self):
        payment = Payment.objects.create(
                payee=self.payee,
                amount = -1245,            
            )
        with self.assertRaises(ValidationError):
            payment.clean()
