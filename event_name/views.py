from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import EventCard
from .serializers import EventCardSerializer
from rest_framework import permissions
# Create your views here.


class EventCardAPIView(ListAPIView):
    queryset = EventCard.objects.all()
    serializer_class = EventCardSerializer
