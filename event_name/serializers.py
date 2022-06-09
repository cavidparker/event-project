from rest_framework import serializers
from .models import EventCard


class EventCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCard
        fields = '__all__'
