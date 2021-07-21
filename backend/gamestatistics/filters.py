#Définition des filtres pour les tableaux de statistiques.

import django_filters
from .models import Rank_awp, Rank_retake


class Rank_awpFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Username', lookup_expr='icontains')
    steam = django_filters.CharFilter(label='SteamID', lookup_expr='icontains')
    class Meta:
        model = Rank_awp
        fields = ['name', 'steam']


class Rank_retakeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Username', lookup_expr='icontains')
    steam = django_filters.CharFilter(label='SteamID', lookup_expr='icontains')
    class Meta:
        model = Rank_retake
        fields = ['name', 'steam']