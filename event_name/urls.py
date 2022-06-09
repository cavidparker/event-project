from django.urls import path
from .views import EventCardAPIView

urlpatterns = [
    path('event_post/', EventCardAPIView.as_view(), name='event-post')
]
