from django.db import models


# Create your models here.

""" Class used to create the Account Model structure"""
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    studentId = models.CharField(max_length=8, unique=True)
    hasOutstandingBalance = models.BooleanField(default=0)

""" Class used to create the Status Enum"""
class Status(models.TextChoices):
    OUTSTANDING = 'OUTSTANDING'
    PAID = 'PAID'
    CANCELLED = 'CANCELLED'

""" Class used to create the Type Enum"""
class Type(models.TextChoices):
    LIBRARY_FINES = 'L', 'LIBRARY FINES'
    TUITION_FEES = 'T', 'TUITION FEES'

""" Class used to create the Invoice Model structure"""
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=8, unique=True)
    amount = models.FloatField(max_length=50)
    dueDate = models.DateField(max_length=50)
    status = models.CharField(choices=Status.choices, max_length=50)
    type = models.CharField(choices=Type.choices, max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='studentId')
