from django.urls import path
from .api_views import *


urlpatterns = [
	path('', SteamAPI.as_view(), name="steamuserinfo")
]