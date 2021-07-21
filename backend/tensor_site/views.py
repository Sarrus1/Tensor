from django.shortcuts import render
import markdown2
from .models import News
from servers.models import Server, PlayerCount
from django.views.generic import TemplateView

import time

from steamwebapi.api import ISteamUser
from django.shortcuts import render
from authentication.models import SteamUser
import tensor_site.auth_tokens
from sourcebans.models import SbBans, SbAdmins
from internal_stats.models import InternalStats


steamuserinfo = ISteamUser(steam_api_key=tensor_site.auth_tokens.SteamWebAPIKey)


class indexView(TemplateView):
		template_name = "tensor_site/index.html"

		def get_context_data(self, **kwargs):
				context = super().get_context_data(**kwargs)
				servers = []
				serversQuery = Server.objects.all()
				for server in serversQuery:
					query = PlayerCount.objects.filter(server=server).order_by("-id").first()
					if query is not None:
						ip = server.connectionInfo
						playerdata = {
						'map': query.current_map,
						'players': query.player_count,
						'adress': "steam://connect/{}".format(ip),
						'max': query.max_player,
						'percent': "{}%".format(int(query.player_count/query.max_player*100)),
						'ip': ip,
						}
						servers.append({
								"server": server,
								"data": playerdata
						})
				context["servers"] = servers

				news = News.objects.all().order_by('-date').first()
				if news is not None:
					news.content=markdown2.markdown(news.content)
				else:
					news = "null"
				context["news"] = news

				bans = []
				myresult = SbBans.objects.all().order_by('-created')[:len(servers)]
				for ban in myresult:
					length = ban.length
					if length == 0:
							length = "Permanent"
					elif length <= 84600:
							length = time.strftime('%Hh:%Mm', time.gmtime(length))
					else:
							length = str(length//84600) + " days"
					bans.append({
							"Name": ban.name,
							"SteamID": ban.authid,
							"Length": ban.duration,
					})
				context["bans"] = bans
				total_servers = serversQuery.count()
				total_bans, total_players, total_time = 0, 0, 0
				LastInternalStats = InternalStats.objects.all().order_by("-id").first()
				if LastInternalStats is not None:
					total_bans = LastInternalStats.total_bans
					total_players = LastInternalStats.total_users
					total_time = LastInternalStats.days_played

				context["stats"] = {
					"total_bans": total_bans,
					"total_players": total_players,
					"total_time": total_time,
					"total_servers": total_servers
				}
				return context


class newsView(TemplateView):
		template_name = "tensor_site/news.html"

		def get_context_data(self, **kwargs):
				context = super().get_context_data(**kwargs)
				news = News.objects.all().order_by('-date')
				for new in news:
					new.content=markdown2.markdown(new.content)
				context["news"] = news
				return context
		

class adminsView(TemplateView):
		template_name = 'tensor_site/admins.html'

		def get_context_data(self, **kwargs):
				context = super().get_context_data(**kwargs)
				admins = []
				q = SbAdmins.objects.all()
				for admin in q:
					steamid64 = admin.steamid64()
					User = SteamUser.objects.filter(steamid=steamid64).first()
					if User is None:
						continue
					admins.append(
						{
							"steamid": admin.authid,
							"group": "",
							"link": User.profileurl,
							"avatar": User.avatarmedium,
							"name": User.personaname,
							"country": User.loccountrycode
						}
					)
				context["admins"] = admins
				return context


class serverRulesView(TemplateView):
		template_name = "tensor_site/server-rules.html"
