from multiselectfield import MultiSelectField
from django.db import models
from PIL import Image
from tinymce import models as tinymce_models
# Create your models here.


class EventCard(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    date_and_time = models.DateTimeField()
    organisers_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)
    followers = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    online_type = models.CharField(max_length=200, null=True, blank=True)
    map_lat = models.CharField(max_length=200, null=True, blank=True)
    map_long = models.CharField(max_length=200)
    refund_policy = models.CharField(max_length=200, null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    description = tinymce_models.HTMLField(
        max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.title


class TicketSelection(models.Model):
    title = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    tax = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    eventcard = models.ForeignKey(
        EventCard, on_delete=models.CASCADE, related_name='ticket_pattern_list')

    def __str__(self):
        return self.title
