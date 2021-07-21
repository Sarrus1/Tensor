#Définition des filtres pour les tableaux des bans.

import django_filters
from .models import SbBans

class SbBans_Filter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Name', lookup_expr='icontains')
    authid = django_filters.CharFilter(label='SteamID', lookup_expr='icontains')
    ip = django_filters.CharFilter(label='IP', lookup_expr='icontains')
    class Meta:
        model = SbBans
        fields = ['name', 'authid', 'ip']