from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    confirm_email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200)
    Expiration_date = models.CharField(max_length=200)
    csc = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class Paypal(models.Model):
    country = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    cvv = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    apt_suite = models.CharField(
        max_length=200, blank=True, null=True, default=False)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class GooglePay(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=25)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    cvc = models.CharField(max_length=50)
    cardholder_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)

    def __str__(self):
        return self.cardholder_name
