from django.urls import path
from . import views



urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('portal', views.portal, name='portal'),
    path('portal/invoice/<str:reference>', views.invoice, name='invoice'),
    path('api/invoice/all', views.getAllInvoice, name='FindAll'),
    path('api/invoice/<int:invoiceID>', views.getInvoiceByID , name='FindByID'),
    path('portal/invoice/<str:reference>/PAID', views.PayInvoice, name='PayInvoice')
]