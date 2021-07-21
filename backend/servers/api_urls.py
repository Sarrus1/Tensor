from django.urls import path, include
from rest_framework import routers
from .api_views import *

router = routers.DefaultRouter()
router.register('', ServersViewSet)

urlpatterns = [
	path('playercount/', PlayerCountView.as_view(), name='servers-playercount'),
	path('servers-control/', ServerControlView.as_view(), name='servers-control'),
	path('', include(router.urls)),

]