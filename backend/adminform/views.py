from django.shortcuts import render
from django.core.mail import send_mail
# Models
from .models import *
from authentication.models import SteamUser
from sourcebans.models import SbBans, SbAdmins
from gamestatistics.models import Rank_awp, Rank_retake

from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tensor_site.decorators import login_required_message
from django.http import HttpResponseRedirect

import tensor_site.auth_tokens
from steamwebapi.api import ISteamUser
from .admin import AddToSourcebans, mail_accept_message
from discord_webhook import DiscordWebhook, DiscordEmbed


# Utils
from steam.steamid import SteamID


def IsStaff(steamid):
	query = SbAdmins.objects.get(authid=steamid)
	if query:
			return True
	return False

steamuserinfo = ISteamUser(steam_api_key=tensor_site.auth_tokens.SteamWebAPIKey)

@login_required_message
@login_required
def ModeratorApplicationView(request):
	commid = str(request.user.steamid)
	steamid = SteamID(commid).as_steam2
	application = ApplicationModel.objects.filter(SteamID=steamid).order_by('-Date')
	if application:
		if application[0].Status == 'Rejected' or application[0].Status == 'Pending':
			messages.success(request, 'You can only apply once.', extra_tags='danger')
			return HttpResponseRedirect('/')
		else:
			form = ApplicationForm()
			return render(request, "adminform/moderator_application.html", {'form': form})
	else:
		if request.method == 'POST':
			form = ApplicationForm(request.POST)
			if form.is_valid():
				commid = str(request.user)
				application = form.save(commit=False)
				application.SteamID = steamid
				application.Name = SteamUser.objects.get(steamid=commid).personaname
				form.save()
				send_mail(
						'New Moderator application',
						'A new application has been submitted.',
						'information@tensor.fr',
						[tensor_site.auth_tokens.adminEmail],
						fail_silently=False,
				)
				#Discord webhook message
				webhook = DiscordWebhook(url=tensor_site.auth_tokens.Discord_Webhook_Moderation)
				embed = DiscordEmbed(title='A new Moderator Application has been submitted.',
				 description='There is a new Moderator Application. Admins with the appropriate permission level can process it on the website.',
					color=242424,
					url="http://data.tensor.fr/moderator-application-validation/%s/%s" % (steamid, application.Server))
				embed.add_embed_field(name='Server', value=application.Server.upper(), inline=True)
				embed.add_embed_field(name='Player Name', value=str(SteamUser.objects.get(steamid=commid).personaname), inline=True)
				user_stats = Rank_awp.objects.get(steam__contains=str(steamid[8:]))
				score = user_stats.score
				embed.add_embed_field(name='Points', value=str(score), inline=True)
				embed.set_thumbnail(url=str(request.user.avatarfull))
				#embed.image = request.user.avatarfull
				webhook.add_embed(embed)
				response = webhook.execute()

				messages.success(request, 'Your application has been submitted.', extra_tags='success')
				return HttpResponseRedirect("/")
		else:
				form = ApplicationForm()
		return render(request, "adminform/moderator_application.html", {'form': form})



@login_required_message
@login_required
def ModeratorApplicationListView(request):
	if not IsStaff(request.user.steamid2):
		messages.success(request, "You don't have permission to do that.", extra_tags='danger')
		return HttpResponseRedirect("/")
	ApplicationList = []
	if request.user.can_accept_awp and request.user.can_accept_retake:
		queryset = ApplicationModel.objects.all().order_by('-Date')
		for application in queryset:
			ApplicationList.append({
				"Name": application.Name,
				"Server": application.Server.upper(),
				"Button": "/moderator-application-validation/%s/%s" % (application.SteamID, application.Server),
				"Status": application.Status
		})
	elif request.user.can_accept_awp:
		queryset = ApplicationModel.objects.filter(Server="awp").order_by('-Date')
		for application in queryset:
			ApplicationList.append({
				"Name": application.Name,
				"Server": application.Server.upper(),
				"Button": "/moderator-application-validation/%s/%s" % (application.SteamID, application.Server),
				"Status": application.Status
		})
	elif request.user.can_accept_retake:
		queryset = ApplicationModel.objects.filter(Server="retake").order_by('-Date')
		for application in queryset:
			ApplicationList.append({
				"Name": application.Name,
				"Server": application.Server.upper(),
				"Button": "/moderator-application-validation/%s/%s" % (application.SteamID, application.Server),
				"Status": application.Status
			})
	return render(request, "adminform/moderator-application-list.html", {"ApplicationList": ApplicationList})


@login_required_message
@login_required
def ModeratorApplicationValidationView(request, steamid, server_name):
	if not IsStaff(request.user.steamid2):
		messages.success(request, "You don't have permission to do that.", extra_tags='danger')
		return HttpResponseRedirect("/")
	application = ApplicationModel.objects.get(Server=server_name, SteamID=steamid)
	steamid64 = SteamID(steamid).as_64
	user_info = SteamUser.objects.get(steamid=steamid64)
	if server_name == "awp":
		user_stats = Rank_awp.objects.get(steam__contains=steamid[8:])
		score = user_stats.score
		playtime = user_stats.time()
	elif server_name == "retakes":
		user_stats = Rank_retake.objects.get(steam__contains=steamid[8:])
		score = user_stats.score
		playtime = user_stats.time()
	else:
		playtime = "Unknown"
		score = "Unknown"

	bans = SbBans.objects.filter(authid__contains=steamid[8:]).count()
	user = SteamUser.objects.filter(steamid=SteamID(steamid).as_64)[0]
	application_dic = {
    "Server": application.Server,
    "Email": application.Email,
    "Discord": application.Discord,
    "Age": application.Age,
    "Experience": application.Experience,
    "Experience_more": application.Experience_more,
    "Reason": application.Reason,
    "SteamID": steamid,
    "Name": application.Name,
    "Date": application.Date,
    "Status": application.Status,
    "Picture_url": user_info.avatar,
    "Profile_url": user_info.profileurl,
    "Country_code": user.loccountrycode,
		"Playtime": playtime,
		"Points": score,
		"Bans": bans,
		"Accept_url": "/moderator-application-accept/{}/{}".format(application.SteamID, application.Server),
		"Reject_url": "/moderator-application-reject/{}/{}".format(application.SteamID, application.Server)
  }
	return render(request, "adminform/moderator_application_validation.html", application_dic)



@login_required_message
@login_required
def AcceptApplication(request, steamid, server_name):
	if not request.user.can_accept_awp and server_name == 'awp':
		messages.success(request, "You don't have permission to do that.", extra_tags='danger')
		return HttpResponseRedirect("/")
	elif not request.user.can_accept_retake and server_name == 'retake':
		messages.success(request, "You don't have permission to do that.", extra_tags='danger')
		return HttpResponseRedirect("/")
	application = ApplicationModel.objects.get(Server=server_name, SteamID=steamid)
	if application.Status == 'Pending':
			application.Status = 'Accepted'
			application.save()
			send_mail(
			'Moderator application',
			'',
			'information@tensor.fr',
			[application.Email],
			fail_silently=False,
			html_message=mail_accept_message
			)
			#Discord webhook message
			webhook = DiscordWebhook(url=tensor_site.auth_tokens.Discord_Webhook_Moderation)
			embed = DiscordEmbed(title='A new Moderator has been accepted.',
				description='A new moderator has joined the team! Please make sure to welcome them!',
				color=242424)
			embed.add_embed_field(name='Server', value=application.Server.upper(), inline=True)
			embed.add_embed_field(name='Player Name', value=application.Name, inline=True)
			user_stats = Rank_awp.objects.get(steam__contains=steamid[8:])
			score = user_stats.score
			embed.add_embed_field(name='DiscordID', value=application.Discord, inline=True)
			embed.set_thumbnail(url=str(request.user.avatarfull))
			webhook.add_embed(embed)
			response = webhook.execute()
			messages.success(request, 'Successfuly accepted new Moderator', extra_tags='success')
			AddToSourcebans(application.SteamID,  application.Email, "Moderators", application.Server)
	return HttpResponseRedirect("/")


@login_required_message
@login_required
def RefuseApplication(request, steamid, server_name):
	if not request.user.can_accept_awp and server_name == 'awp':
		messages.success(request, "You don't have permission to do that.", extra_tags='danger')
		return HttpResponseRedirect("/")
	elif not request.user.can_accept_retake and server_name == 'retake':
		messages.success(request, "You don't have permission to do that.", extra_tags='danger')
		return HttpResponseRedirect("/")
	application = ApplicationModel.objects.get(Server=server_name, SteamID=steamid)
	if application.Status == 'Pending':
		application.Status = 'Rejected'
		application.save()
		messages.success(request, 'Successfuly rejected Application', extra_tags='warning')
	return HttpResponseRedirect("/")