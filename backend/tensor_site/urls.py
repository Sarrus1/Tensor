from .views import *
from django.urls import path

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('news/', newsView.as_view(), name='news'),
    path('admins/', adminsView.as_view(), name='admins'),
    path("server-rules/", serverRulesView.as_view(), name="server-rules"),
]