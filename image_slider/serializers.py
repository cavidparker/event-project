from rest_framework import serializers
from .models import Imageheader


class ImageheaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imageheader
        fields = '__all__'
