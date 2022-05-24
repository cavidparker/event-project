from django.db import models

# Create your models here.


class Imageheader(models.Model):
    image = models.ImageField(upload_to='images')
    help_title = models.CharField(max_length=200)
    help_description = models.CharField(max_length=200)

    def __str__(self):
        return self.help_title
