from django.urls import path
from .views import *

urlpatterns = [
		path('stats-awp/', Rank_awpListView.as_view()),
    path('stats-retake/', Rank_retakeListView.as_view()),
    path('stats/awp/<str:steamid>', AwpStatsView, name='awp_stats'),
    path('stats-surf/', SurfStatsView.as_view(), name='surf_stats'),
    path('stats/retake/<str:steamid>', RetakesStatsView, name='retake_stats'),
]
