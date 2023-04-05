from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Finance.forms import Invoice_Form
from rest_framework import response
from .serializers import InvoiceSerializers
from .models import Invoice, Account


# Create your views here.

def portal(request):
    form = Invoice_Form()
    context = {'form': form}
    return render(request, "portal.html",context)

def redirect(request):
    return HttpResponseRedirect('/portal')

def invoice(request):
    return render(request, "invoice.html")


@api_view(['GET'])
def getAllInvoice(request):
    items = Invoice.objects.all()
    serializer = InvoiceSerializers(items, many=True)
    return Response(serializer.data)