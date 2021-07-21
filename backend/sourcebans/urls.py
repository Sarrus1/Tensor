from django.urls import path
from .views import *

urlpatterns = [
  path('bans/', BansView.as_view(), name='bans-list'),
  path('bans/<str:steamid>', BansView.as_view(), name='bans-list'),
  path('ban-protest/', BanProtestView.as_view(), name='ban-protest')
]