from django.urls import path, include
from rest_framework import routers
from .api_views import *

router = routers.DefaultRouter()
router.register('', BansViewSet)

urlpatterns = [
	path('', include(router.urls)),
  path('kick-from-server/<str:steamid>', KickFromServerView.as_view(), name="kick-from-server")
]