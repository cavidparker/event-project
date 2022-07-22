from django.contrib import admin
from .models import EventCard, TicketSelection
# Register your models here.
admin.site.register(TicketSelection)
admin.site.register(EventCard)
