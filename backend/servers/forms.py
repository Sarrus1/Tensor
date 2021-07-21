from django import forms
from .models import ServerControlModel


class ServerControlForm(forms.ModelForm):
		command = forms.CharField()
		port = forms.IntegerField()
		
		class Meta:
				model = ServerControlModel
				fields = ['uuid', 'command', 'port']
				exclude = ['status', 'output']
