from django.test import SimpleTestCase
from .forms import Invoice_Form


class InvoiceFormTest(SimpleTestCase):

    def test_valid_form(self):
        form = Invoice_Form(data={
        'reference': "TSDF21AS"
        })
        self.assertTrue(form.is_valid())

    def test_form_Empty_String_reference(self):
        form = Invoice_Form(data={
            'reference': ""
        })
        self.assertFalse(form.is_valid())

    def test_form_with_too_small_reference(self):
            form = Invoice_Form(data={
                'reference': "SD31"
            })
            self.assertFalse(form.is_valid())

    def test_form_with_too_big_reference(self):
            form = Invoice_Form(data={
                'reference': "SD3SHJSADJ134ES1"
            })
            self.assertFalse(form.is_valid())

    def test_form_with_not_string_value_reference(self):
        form = Invoice_Form(data={
            'reference': 122433242
        })
        self.assertFalse(form.is_valid())

    def test_form_with_null_reference(self):
            form = Invoice_Form(data={
                'reference': None
            })
            self.assertFalse(form.is_valid())



