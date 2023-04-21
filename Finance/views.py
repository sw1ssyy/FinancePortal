import json
import random
import string
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Finance.forms import Invoice_Form
from .models import Invoice, Status, Account
from .serializers import InvoiceSerializers, AccountSerializer


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
        return render(request, 'invoiceNotFound.html')


def PayInvoice(request, reference):
    GraduationStatus = 0
    data = Invoice.objects.get(reference=reference)
    data.status = Status.PAID
    data.save()
    acc = Invoice.objects.filter(account_id=data.account_id)
    acc2 = Account.objects.get(studentId=data.account_id)
    for i in acc:
        print(i.status,i.reference)
        if i.status == Status.OUTSTANDING:
            GraduationStatus = GraduationStatus + 1

    print(acc2.studentId,acc2.hasOutstandingBalance)
    if GraduationStatus == 0:
        acc2.hasOutstandingBalance = False
        acc2.save()
        print(acc2.studentId + " Is Good to Graduate!!")

    return HttpResponseRedirect('/portal/invoice/' + reference)


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


@api_view(['POST'])
def createStudentFinanceAccount(request):
    if request.method == 'POST':
        accountdata = json.loads(request.body)
        studentId = accountdata.get('studentId')
        newAccount = Account.objects.create(studentId=studentId, hasOutstandingBalance=False)
        serializer = AccountSerializer(newAccount, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def createNewInvoice(request):
    if request.method == 'POST':
        invoicedata = json.loads(request.body)
    amount = invoicedata.get('amount')
    date = invoicedata.get('dueDate')
    type = invoicedata.get('type')
    studentID = invoicedata.get('account', {}).get('studentId')

    newInvoice = Invoice.objects.create(
        reference=createReferenceID(),
        amount=amount,
        dueDate=date,
        type=type,
        account_id=studentID,
        status=Status.OUTSTANDING
    )
    serializer = InvoiceSerializers(newInvoice, many=False)
    targetaccount = Account.objects.get(studentId=studentID)
    targetaccount.hasOutstandingBalance = True
    targetaccount.save()
    return Response(serializer.data)

@api_view(['GET'])
def getAccountByStudentID(request, studentID):
    account_data = Account.objects.get(studentId=studentID)
    serializer = AccountSerializer(account_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAllAccounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


# Redirects
def redirect(request):
    return HttpResponseRedirect('/portal')


# Creating Reference ID
def createReferenceID():
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(8))
