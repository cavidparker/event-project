from django.urls import path
from .views import EventCardAPIView, TicketSelectionAPIView, EventCardDetailsAPIView

urlpatterns = [
    path('ticket_post/', TicketSelectionAPIView.as_view(), name='ticket-post'),
    path('event_post/', EventCardAPIView.as_view(), name='event-post'),
    path('event_post/<slug>/', EventCardDetailsAPIView.as_view(),
         name='event-details'),

]
