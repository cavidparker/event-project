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
    location = models.CharField(max_length=200)
    followers = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    online_type = models.CharField(max_length=200)
    map_lat = models.CharField(max_length=200)
    map_long = models.CharField(max_length=200)
    refund_policy = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    description = tinymce_models.HTMLField(max_length=10000)

    def __str__(self):
        return self.title
