from django.test import TestCase
from .models import Account, Invoice, Status, Type


# Create your tests here.


class AccountTests(TestCase):
    def setUp(self):
        self.testacc1 = Account.objects.create(
            id=1,
            studentId="c1234567",
            hasOutstandingBalance=False)

    def testAccountCreation(self):
        self.assertEqual(self.testacc1.studentId, 'c1234567')


class InvoiceTests(TestCase):
    def setUp(self):
        self.testacc1 = Account.objects.create(
            id=1,
            studentId="c1234567",
            hasOutstandingBalance=False)

        self.testInvoice = Invoice.objects.create(
            id=1,
            reference="SFCJAW1A",
            amount=20.00,
            dueDate= str('2006-10-25'),
            status=Status.OUTSTANDING,
            type=Type.TUITION_FEES,
            account_id="c1234567"
        )
    def testInvoiceCreation(self):
        self.assertEqual(self.testInvoice.reference, "SFCJAW1A")