from rest_framework import serializers
from .models import EventCard, TicketSelection


class TicketSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketSelection
        fields = ['id', 'title', 'price', 'tax', 'description', 'eventcard']


class EventCardSerializer(serializers.ModelSerializer):
    ticket_pattern_list = TicketSelectionSerializer(many=True, read_only=True)

    class Meta:
        model = EventCard
        fields = '__all__'
