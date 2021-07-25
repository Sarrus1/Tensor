from django.urls import path, include
from rest_framework import routers
from .api_views import *

router = routers.DefaultRouter()
router.register('', BansViewSet)

urlpatterns = [
	path('kick-from-server/', KickFromServerView.as_view(), name="kick-from-server"),
	path('', include(router.urls)),
  
]