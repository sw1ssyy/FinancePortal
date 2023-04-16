from rest_framework import serializers
from Finance.models import Invoice, Account


class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'