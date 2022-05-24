from django.urls import path
from .views import ImageheaderAPIView

urlpatterns = [
    path('images/', ImageheaderAPIView.as_view(), name='image-post')
]
