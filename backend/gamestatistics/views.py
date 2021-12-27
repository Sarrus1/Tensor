from django.shortcuts import render
from django.http import Http404
from .models import *
from .tables import *
from .tables import Rank_awpTable, Rank_retakeTable
from .filters import Rank_awpFilter, Rank_retakeFilter

from django.views.generic import TemplateView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class Rank_awpListView(SingleTableMixin, FilterView):
    model = Rank_awp
    table_class = Rank_awpTable
    template_name = 'gamestatistics/stats-awp.html'
    filterset_class = Rank_awpFilter


class Rank_retakeListView(SingleTableMixin, FilterView):
    model = Rank_retake
    table_class = Rank_retakeTable
    template_name = 'gamestatistics/stats-retake.html'
    filterset_class = Rank_retakeFilter


class SurfStatsView(TemplateView):

    template_name = 'gamestatistics/stats_surf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        times = []
        myresult = CkPlayertimes.objects.raw(
            """
				SELECT t.mapname, t.runtimepro, t.name, t.steamid 
				FROM (
					SELECT mapname, MIN(runtimepro) as minruntimepro FROM `ck_playertimes` GROUP BY mapname) 
					AS x 
					INNER JOIN ck_playertimes AS t 
					ON t.mapname=x.mapname AND t.runtimepro=x.minruntimepro
				"""
        )
        for result in myresult:
            time = result.runtimepro
            minute = time//60
            second = int(time-minute*60)
            ms = int((time-minute*60-second)*1000)
            time = "{}:{}:{}".format(minute, second, ms)
            times.append(
                {
                    "mapname": result.mapname,
                    "time": time,
                    "name": result.name,
                    "steamid": result.steamid
                }
            )

        context["times"] = times
        return context


def AwpStatsView(request, steamid):
    user = Rank_awp.objects.filter(steam=steamid).first()
    if user is not None:
        raise Http404("Steamid does not exist")
    playtime = user.time()
    if user.deaths == 0:
        KD = str(round(user.kills, 2))
    else:
        KD = str(round(user.kills/user.deaths, 2))
    if user.rounds_ct + user.rounds_tr == 0:
        ADR = str(round(user.damage, 2))
    else:
        ADR = str(round(user.damage/(user.rounds_ct + user.rounds_tr), 2))
    if user.kills == 0:
        HS = str(round(0, 2)*100)+" %"
    else:
        HS = str(round(user.headshots/user.kills, 2)*100)+" %"
    stats = {
        "name": user.name,
        "score": user.score,
        "kills": user.kills,
        "deaths": user.deaths,
        "KD": KD,
        "ADR": ADR,
        "HS": HS,
        "hits": user.hits,
        "shots": user.shots,
        "head": user.headshots,
        "chest": user.chest,
        "stomach": user.stomach,
        "left_arm": user.left_arm,
        "right_arm": user.right_arm,
        "left_leg": user.left_leg,
        "right_leg": user.right_leg,
        "playtime": playtime
    }
    return render(request, 'gamestatistics/stats-awp-player.html', stats)


def RetakesStatsView(request, steamid):
    user = Rank_retake.objects.filter(steam=steamid).first()
    if user is not None:
        raise Http404("Steamid does not exist")
    playtime = user.time()
    if user.deaths == 0:
        KD = str(round(user.kills, 2))
    else:
        KD = str(round(user.kills/user.deaths, 2))
    if user.rounds_ct + user.rounds_tr == 0:
        ADR = str(round(user.damage, 2))
    else:
        ADR = str(round(user.damage/(user.rounds_ct + user.rounds_tr), 2))
    if user.kills == 0:
        HS = "{} %".format(round(0, 2)*100)
    else:
        HS = "{} %".format(round(user.headshots/user.kills, 2)*100)
    stats = {
        "name": user.name,
        "score": user.score,
        "kills": user.kills,
        "deaths": user.deaths,
        "KD": KD,
        "ADR": ADR,
        "HS": HS,
        "hits": user.hits,
        "shots": user.shots,
        "head": user.headshots,
        "chest": user.chest,
        "stomach": user.stomach,
        "left_arm": user.left_arm,
        "right_arm": user.right_arm,
        "left_leg": user.left_leg,
        "right_leg": user.right_leg,
        "knife": user.knife,
        "glock": user.glock,
        "hkp2000": user.hkp2000,
        "usp_silencer": user.usp_silencer,
        "p250": user.p250,
        "deagle": user.deagle,
        "elite": user.elite,
        "fiveseven": user.fiveseven,
        "tec9": user.tec9,
        "cz75a": user.cz75a,
        "revolver": user.revolver,
        "nova": user.nova,
        "xm1014": user.xm1014,
        "mag7": user.mag7,
        "sawedoff": user.sawedoff,
        "bizon": user.bizon,
        "mac10": user.mac10,
        "mp9": user.mp9,
        "mp7": user.mp7,
        "ump45": user.ump45,
        "p90": user.p90,
        "galilar": user.galilar,
        "ak47": user.ak47,
        "famas": user.famas,
        "m4a1": user.m4a1,
        "m4a1_silencer": user.m4a1_silencer,
        "aug": user.aug,
        "ssg08": user.ssg08,
        "sg556": user.sg556,
        "awp": user.awp,
        "hegrenade": user.hegrenade,
        "inferno": user.inferno,
        "playtime": playtime
    }
    return render(request, 'gamestatistics/stats-retake-player.html', stats)
