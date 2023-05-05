from django import forms

"""Class used to create the input form for entering the Invoice reference"""
class Invoice_Form(forms.Form):
    reference = forms.CharField(max_length=8, min_length=8, required=True)
