from django.urls import path, include
from .views import *

urlpatterns = [
    path('donations/', DonationsView.as_view(), name='donations'),
    path("paypal/", include('paypal.standard.ipn.urls')),
    path("paypal-return/", PaypalReturnView, name="paypal-return"),
    path("paypal-cancel/", PaypalCancelView, name="paypal-cancel"),
]