from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contact, Paypal, GooglePay
from .serializers import ContactSerializer, PaypalSerializer, GooglePaySerializer

# Create your views here.


class ContactView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaypalView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        paypals = Paypal.objects.all()
        serializer = PaypalSerializer(paypals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaypalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        paypal = Paypal.objects.get(pk=pk)
        serializer = PaypalSerializer(paypal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        paypal = Paypal.objects.get(pk=pk)
        paypal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GooglePayView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        googlepays = GooglePay.objects.all()
        serializer = GooglePaySerializer(googlepays, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GooglePaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
