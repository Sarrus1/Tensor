from django import forms
from tensor_site.validators import validate_steamid

class DonationForm(forms.Form):
    SteamID = forms.CharField(label='SteamID', validators=[validate_steamid])
    amount = forms.IntegerField(label='Donation amount', min_value=1, max_value=100)