from django.shortcuts import render
from django.views.generic import FormView
from steam.steamid import SteamID
from steamwebapi.api import ISteamUser
from django.http import HttpResponseRedirect
from paypal.standard.forms import PayPalPaymentsForm
from .forms import DonationForm
import datetime
from dateutil.relativedelta import relativedelta
from django.views.decorators.csrf import csrf_exempt
from tensor_site.auth_tokens import *
from django.conf import settings

steamuserinfo = ISteamUser(steam_api_key=SteamWebAPIKey)


class DonationsView(FormView):
		template_name = 'donations/donations.html'
		form_class = DonationForm
		success_url = '/ban'

		def post(self, request, *args, **kwargs):
			form = DonationForm(request.POST)
			if form.is_valid():
				return HttpResponseRedirect("/donations-validation/{}/{}".format(form.cleaned_data["SteamID"], form.cleaned_data["amount"]))
		
		def get_context_data(self, **kwargs):
				context = super().get_context_data(**kwargs)
				context["clientID"] = paypalClientID
				return context


@csrf_exempt
def PaypalReturnView(request):
		return render(request, "donations/paypal_return.html", {"post": request.POST, "get": request.GET})

@csrf_exempt
def PaypalCancelView(request):
		return render(request, "donations/paypal_cancel.html", {"post": request.POST, "get": request.GET})

