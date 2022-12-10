from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    birthday = models.DateField()
    address = models.OneToOneField('Address', on_delete=models.CASCADE)

class Address(models.Model):
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
