from django.shortcuts import render
from django.views.generic import FormView
from steamwebapi.api import ISteamUser
from django.http import HttpResponseRedirect
from .forms import DonationForm
from django.views.decorators.csrf import csrf_exempt
from os import getenv

steamuserinfo = ISteamUser(steam_api_key=getenv("STEAM_API_KEY"))


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
        context["clientID"] = getenv("PAYPAL_CLIENT_ID")
        return context


@csrf_exempt
def PaypalReturnView(request):
    return render(request, "donations/paypal_return.html", {"post": request.POST, "get": request.GET})


@csrf_exempt
def PaypalCancelView(request):
    return render(request, "donations/paypal_cancel.html", {"post": request.POST, "get": request.GET})
