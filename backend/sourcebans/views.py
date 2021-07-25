from django.views.generic import TemplateView, FormView
from django.utils.timezone import localtime
from time import mktime
from django.db.models import Q

from .models import *

from discord_webhook import DiscordWebhook, DiscordEmbed

from .forms import BanProtest

from django.contrib.auth.decorators import login_required
from tensor_site.decorators import login_required_message
from tensor_site.auth_tokens import *
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponseRedirect

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class BansView(TemplateView):
		template_name = 'sourcebans/bans.html'

		def get_context_data(self, **kwargs):
				is_admin = 0
				steamid2 = ""
				if(not self.request.user.is_anonymous):
						is_admin = int(self.request.user.is_admin)
						steamid2 = self.request.user.steamid2
				context = super().get_context_data(**kwargs)
				context['is_admin'] = is_admin
				context['steamid2'] = steamid2
				context['search'] = self.kwargs['steamid'] if 'steamid' in self.kwargs else ""
				return context


decorators = [login_required, login_required_message]
@method_decorator(decorators, name='dispatch')
class BanProtestView(FormView):
		template_name = 'sourcebans/ban-protest.html'
		form_class = BanProtest
		success_url = '/ban'

		def post(self, request, *args, **kwargs):
				form = self.get_form()
				steamid=request.user.steamid2
				if form.is_valid():
					matchingBans = SbBans.objects.filter(
						Q(authid__contains=steamid[7:]), Q(Q(ends__gte=mktime(localtime())) | Q(length=0))
						).order_by('-created')
					print(matchingBans.first().ends)
					if(not matchingBans.count() > 0):
						messages.success(request, 'There are no active bans for your steamID.', extra_tags='danger')
						return HttpResponseRedirect("/ban-protest/")
					matchingProtests = SbProtests.objects.filter(bid=matchingBans.first())
					if matchingProtests:
						messages.success(request, 'You cannot appeal a ban more than once.', extra_tags='danger')
						return HttpResponseRedirect("/")
					protest = form.cleaned_data
					newProtest = SbProtests(
						pip = get_client_ip(request),
						bid = matchingBans.first(),
						email = protest["email"],
						reason = protest["reason"]
					)
					newProtest.save()
					sendDiscordMessage(matchingBans.first().bid, matchingBans.first().name, protest["reason"])
					messages.success(request, 'Your ban protest has been submitted and will be processed.', extra_tags='success')
					return HttpResponseRedirect("/")
				else:
						return self.form_invalid(form)


decorators = [login_required, login_required_message]
@method_decorator(decorators, name='dispatch')
class AddBanView(TemplateView):
		template_name = 'sourcebans/ban-add.html'

		def get(self, request, *args, **kwargs):
			if self.request.user.is_admin:
				return super().get(request, *args, **kwargs)
			messages.error(request, "You don't have permission to access this page.", extra_tags='danger')
			return HttpResponseRedirect("/")

def sendDiscordMessage(bid, name, reason):
    webhook = DiscordWebhook(url=Discord_Webhook_Ban_Protest)
    title = 'New ban protest'
    description = ""
    color = 786176
    embed = DiscordEmbed(
			title=title,
			description=description,
			color=color,
			#thumbnail={"url": topAvatarUrl},
			url="https://tensor.fr/sourceban/index.php?p=admin&c=bans#^1",
			)
    embed.add_embed_field(name='Ban ID', value=bid, inline=False)
    embed.add_embed_field(name='Player Name', value=name, inline=False)
    embed.add_embed_field(name='Reason', value=reason, inline=False)
    webhook.add_embed(embed)
    webhook.execute()
    return