from django.db import models

# Create your models here.



class Account(models.Model):
    id=models.BigIntegerField(primary_key=True)
    studentId=models.CharField(max_length=50)
    hasOutstandingBalance=models.BooleanField()

class Status(models.TextChoices):
    OUTSTANDING = 'O', 'OUTSTANDING'
    PAID = 'P', 'PAID'
    CANCELLED = 'C', 'CANCELLED'

class Type(models.TextChoices):
    LIBRARY_FINES = 'L', 'LIBRARY FINES'
    TUITION_FEES = 'T', 'TUITION FEES'
class Invoice(models.Model):
    id=models.BigIntegerField(primary_key=True)
    reference = models.CharField(max_length=8,  unique=True)
    amount = models.FloatField(max_length=50)
    dueDate = models.DateTimeField(max_length=50)
    status = models.CharField(choices=Status.choices, max_length=50)
    type = models.CharField(choices=Type.choices, max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)







