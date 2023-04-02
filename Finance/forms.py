from django import forms


class Invoice_Form(forms.Form):
    invoice = forms.CharField(max_length=8, min_length=8, required=True)
