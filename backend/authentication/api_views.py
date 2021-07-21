from rest_framework import permissions, views, throttling, response
from steam.steamid import SteamID
from steamwebapi.api import ISteamUser
from tensor_site.auth_tokens import *
from django.conf import settings

import re

steamuserinfo = ISteamUser(steam_api_key=SteamWebAPIKey)


class BurstRateThrottle(throttling.UserRateThrottle):
		rate = '5/min'


class SteamAPI(views.APIView):
		"""API endpoint for steam informations query"""
		throttle_classes = [] if settings.DEBUG else [BurstRateThrottle]
		permission_classes = [permissions.IsAuthenticatedOrReadOnly]

		def get(self, request, format=None):
				steamid = ''
				try:
					steamid = request.query_params["steamid"]
					if re.search("^https?\:\/\/steamcommunity.", steamid):
						steamid64 = SteamID.from_url(steamid, 5).as_64
					else:
						steamid64 = SteamID(steamid).as_64
					usersummary = steamuserinfo.get_player_summaries(steamid64)['response']['players'][0]
				except:
					return response.Response(status=500)
				return response.Response(usersummary)