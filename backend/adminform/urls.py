from . import views
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
  path('moderator-application/', views.ModeratorApplicationView, name='moderator_application'),
  path('moderator-application-validation/<str:steamid>/<str:server_name>', views.ModeratorApplicationValidationView, name='moderator_application_validation'),
  path('moderator-application-list/', views.ModeratorApplicationListView, name="moderator-application-list"),
  path('moderator-application-accept/<str:steamid>/<str:server_name>', views.AcceptApplication, name="moderator-application-accept"),
  path('moderator-application-reject/<str:steamid>/<str:server_name>', views.RefuseApplication, name="moderator-application-reject")
]