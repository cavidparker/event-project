from rest_framework import serializers
from .models import Contact, Paypal, GooglePay


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class PaypalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paypal
        fields = '__all__'


class GooglePaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GooglePay
        fields = '__all__'
