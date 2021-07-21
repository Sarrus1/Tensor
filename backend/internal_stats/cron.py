from .models import *
from tensor_site.models import Rank_awp, Rank_retake
from sourcebans.models import SbBans
from django.db.models import Sum

def GetInternalStats():
		# Ranks query
		total_users = 0
		total_users += Rank_awp.objects.all().count()
		total_users += Rank_retake.objects.all().count()

		# Time query
		days_played = 0
		awp_time = Rank_awp.objects.aggregate(Sum("connected"))["connected__sum"]
		if awp_time:
			days_played += awp_time
		retake_time = Rank_retake.objects.aggregate(Sum("connected"))["connected__sum"]
		if retake_time:
			days_played += retake_time
		days_played = days_played//86400

		# Bans query
		total_bans = SbBans.objects.all().count()

		NewInternalStats = InternalStats(total_users=total_users, days_played=days_played, total_bans=total_bans)
		NewInternalStats.save()