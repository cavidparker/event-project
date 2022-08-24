from django.urls import path
from .views import ContactView, PaypalView, GooglePayView


urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('paypal/', PaypalView.as_view(), name='paypal'),
    path('googlepay/', GooglePayView.as_view(), name='googlepay')
]
