from .models import *
from gamestatistics.models import CkPlayertimes, Rank_awp, Rank_retake
from sourcebans.models import SbBans
from django.db.models import Sum

def GetInternalStats():
		awpUsers = Rank_awp.objects.values_list('steam', flat=True)
		retakesUsers = Rank_retake.objects.values_list('steam', flat=True)
		surfUsers = CkPlayertimes.objects.values_list('steamid', flat=True)
		allUsers = awpUsers + retakesUsers + surfUsers
		setAllUsers = set(allUsers)
		total_users = len(setAllUsers)

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