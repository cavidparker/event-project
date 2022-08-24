from django.contrib import admin
from .models import Contact, Paypal, GooglePay

# Register your models here.

admin.site.register(Contact)
admin.site.register(Paypal)
admin.site.register(GooglePay)
