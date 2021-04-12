from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class Stores(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, help_text="name of the store")
    address = models.CharField(max_length=200, help_text="address of the store")
    city = models.ForeignKey( City, on_delete = models.CASCADE, help_text="City")
    phone = models.CharField(max_length=50, help_text="phone number of the store", null=True)

    class Meta:
        ordering = [('city')]

    def __str__(self):
        return self.name

class Medicine(models.Model):

    name = models.CharField(max_length=100, help_text="name of the store")
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Availability(models.Model):

    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.medicine.name}, {self.store.name}"




class FeedBack(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)


    def __str__(self):
        return f"\nFirst name: {self.first_name}\nEmail: {self.email}\nSubject: {self.subject}"


# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
    
#     type_of_customer = [
#         ("C", "Comcumer"),
#         ("P", "Pharmacy")
#     ]

#     customer = models.CharField(
#         max_length = 1,
#         choices=type_of_customer,
#         default="C"
#     )
