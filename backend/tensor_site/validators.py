import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_steamid(value):
    pattern = re.compile("^STEAM_[0-5]:[0-1]:[0-9]*$")
    if not bool(pattern.match(value)):
        raise ValidationError(
            _('%(value)s is not a valid SteamID. Use https://steamid.io/ to get your SteamID'),
            params={'value': value},
        )

def validate_discordid(value):
    pattern = re.compile("(.*)#(\d{4})")
    if not bool(pattern.match(value)):
        raise ValidationError(
            _('%(value)s is not a valid DiscordID.'),
            params={'value': value},
        )
