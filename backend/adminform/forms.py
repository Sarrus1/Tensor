from django import forms
from .models import ApplicationModel
from tensor_site.validators import validate_discordid

SERVER_CHOICES= [
    ('awp', 'AWP'),
    ('retakes', 'Retakes'),
    ('surf', 'Surf'),
    ]

#Définition du formulaire de postulation au rang de modérateur.
class ApplicationForm(forms.ModelForm):

    Discord = forms.CharField(validators=[validate_discordid])
    
    class Meta:
        model = ApplicationModel
        fields = ['Server', 'Email', 'Discord', 'Age', 'Experience', 'Experience_more', 'Reason']
        exclude = ['SteamID', 'Name']
        widgets = {
            'Server': forms.Select(choices=SERVER_CHOICES),
            'Experience': forms.Select(choices=[('no', 'No'), ('yes', 'Yes'), ]),
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['Experience_more'].required = False