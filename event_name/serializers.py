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


class EventCardDetailsSerializer(serializers.ModelSerializer):
    ticket_pattern_list = TicketSelectionSerializer(many=True, read_only=True)
    # slug = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = EventCard
        fields = '__all__'
        # fields = ['id', 'image', 'title', 'slug', 'date_and_time', 'organisers_name', 'location', 'followers',
        #           'country', 'online_type', 'map_lat', 'map_long', 'refund_policy', 'tags', 'description', 'ticket_pattern_list']
        lookup_field = 'slug'
