from django import forms
from .models import SbProtests, SbBans


class BanProtest(forms.Form):
		reason = forms.CharField(widget=forms.Textarea)
		email = forms.EmailField()
