from django.urls import path
from .views import *

urlpatterns = [
    path('servers/', ServerView.as_view(), name='servers')
]
