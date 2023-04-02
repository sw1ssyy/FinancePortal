from django.urls import path
from . import views



urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('portal', views.portal, name='portal'),
    path('portal/invoice', views.invoice, name='invoice')

]