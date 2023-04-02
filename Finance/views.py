from django.shortcuts import render
from django.http import HttpResponseRedirect
from Finance.forms import Invoice_Form

# Create your views here.

def portal(request):
    form = Invoice_Form()
    context = {'form': form}
    return render(request, "portal.html",context)

def redirect(request):
    return HttpResponseRedirect('/portal')

def invoice(request):
    return render(request, "invoice.html")
