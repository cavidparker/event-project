from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    confirm_email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200)
    Expiration_date = models.CharField(max_length=200)
    csc = models.CharField(max_length=200)
    cvv = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
