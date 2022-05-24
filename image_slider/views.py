from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Imageheader
from .serializers import ImageheaderSerializer
from rest_framework import permissions
# Create your views here.


class ImageheaderAPIView(ListAPIView):
    queryset = Imageheader.objects.all()
    serializer_class = ImageheaderSerializer
