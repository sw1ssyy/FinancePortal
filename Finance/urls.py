from django.urls import path
from . import views



urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('portal', views.portal, name='portal'),
    path('portal/invoice/<str:reference>', views.invoice, name='invoice'),
    path('api/invoice/all', views.getAllInvoice, name='FindAllInvoices'),
    path('api/accounts/all', views.getAllAccounts, name='FindAllAccounts'),
    path('api/invoice/search/<int:invoiceID>', views.getInvoiceByID , name='FindInvoiceByID'),
    path('api/accounts/search/<str:studentID>', views.getAccountByStudentID, name='FindAccountByID'),
    path('portal/invoice/<str:reference>/PAID', views.PayInvoice, name='PayInvoice'),
    path('api/accounts/create', views.createStudentFinanceAccount, name='CreateStudentFinanceAccount'),
    path('api/invoice/create', views.createNewInvoice, name='createNewInvoice')
]