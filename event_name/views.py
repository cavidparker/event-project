from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import EventCard, TicketSelection
from .serializers import EventCardSerializer, TicketSelectionSerializer, EventCardDetailsSerializer
from rest_framework import permissions, viewsets
# Create your views here.


# class EventCardAPIView(ListAPIView):
#     queryset = EventCard.objects.all()
#     serializer_class = EventCardSerializer

class EventCardAPIView(ListAPIView):
    queryset = EventCard.objects.all()
    serializer_class = EventCardSerializer
    # permission_classes = [permissions.IsAuthenticated]


class EventCardDetailsAPIView(RetrieveAPIView):
    serializer_class = EventCardDetailsSerializer
    queryset = EventCard.objects.all()
    # queryset = EventCard.objects.filter(
    #     is_published=True).order_by('-list_data')
    lookup_field = 'slug'
    # permission_classes = [permissions.IsAuthenticated]


class TicketSelectionAPIView(ListAPIView):
    queryset = TicketSelection.objects.all()
    serializer_class = TicketSelectionSerializer
    # permission_classes = [permissions.IsAuthenticated]
