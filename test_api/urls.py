from django.urls import path, include
from .views import SingerViewSet, SongViewSet
from rest_framework.routers import DefaultRouter

# creating router objects
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('singer', SingerViewSet, basename='singer')
router.register('song', SongViewSet, basename='song')


urlpatterns = [
    path('test/', include(router.urls)),

]
