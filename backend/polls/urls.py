from django.urls import path
from .views import *

urlpatterns = [
    path('', PollColorsView.as_view(), name='poll-colors'),
]
