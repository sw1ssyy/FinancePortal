from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Finance.forms import Invoice_Form
from .models import Invoice, Status
from .serializers import InvoiceSerializers


# WEB PAGES

# Home Page
def portal(request):
    form = Invoice_Form(request.GET)
    if form.is_valid():
        reference = form.cleaned_data['reference']
        print(reference)
        return HttpResponseRedirect('/portal/invoice/' + reference)
    return render(request, "portal.html", {'form': form})


# Viewing Invoice
def invoice(request, reference):
    try:
        data = Invoice.objects.get(reference=reference)
        return render(request, "invoice.html", {'Invoice': data})
    except Invoice.DoesNotExist:
        return render(request,'invoiceNotFound.html')


# APIS

@api_view(['GET'])
def getAllInvoice(request):
    items = Invoice.objects.all()
    serializer = InvoiceSerializers(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getInvoiceByID(request, invoiceID):
    invoice_data = Invoice.objects.get(pk=invoiceID)
    serializer = InvoiceSerializers(invoice_data, many=False)
    return Response(serializer.data)


def PayInvoice(request, reference):
    data = Invoice.objects.get(reference=reference)
    data.status = Status.PAID
    data.save()
    return HttpResponseRedirect('/portal/invoice/' + reference)
# Redirects
def redirect(request):
    return HttpResponseRedirect('/portal')
