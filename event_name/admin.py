from django.contrib import admin
from .models import EventCard, TicketSelection


# class EventCardAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(TicketSelection)
admin.site.register(EventCard)
