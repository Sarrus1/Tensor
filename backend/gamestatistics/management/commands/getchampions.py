﻿from django.core.management.base import BaseCommand
from discord_webhook import DiscordWebhook, DiscordEmbed
from gamestatistics.models import *
from django.utils import timezone
from steamwebapi.api import ISteamUser
from steam.steamid import SteamID
from os import getenv

steamuserinfo = ISteamUser(steam_api_key=getenv("STEAM_API_KEY"))


def sendDiscordMessage(players, topAvatarUrl):
    webhook = DiscordWebhook(url=getenv("DISCORD_WEBHOOK_AWP_RANK"))
    title = '🏆 Champions of the day 🏆'
    description = "The following players have the **highest score** on the AWP server for this season, as of today."
    color = 786176
    embed = DiscordEmbed(
        title=title,
        description=description,
        color=color,
        thumbnail={"url": topAvatarUrl},
        url="https://tensor.fr/stats-awp/",
        footer={
            "text": "Get your stats on our website! 📈",
            "icon_url": "https://img.icons8.com/color-glass/48/000000/domain.png"
        }
    )
    embed.add_embed_field(name='🥇1st place', value=players[0])
    embed.add_embed_field(name='🥈2nd place', value=players[1])
    embed.add_embed_field(name='🥉3rd place', value=players[2])
    webhook.add_embed(embed)
    webhook.execute()
    return


def preparePlayers(players):
    preparedPlayers = []
    for player in players:
        url = "https://tensor.fr/stats/awp/{}".format(player.steam)
        preparedPlayers.append(
            "[{}]({}) **{}** _pts_".format(player.name, url, player.score)
        )
    topAvatarUrl = steamuserinfo.get_player_summaries(SteamID(players[0].steam).as_64)[
        'response']['players'][0]["avatarmedium"]
    return preparedPlayers, topAvatarUrl


class Command(BaseCommand):
    help = 'Get the champions of the day'

    def handle(self, *args, **options):
        now = timezone.now()
        season = RankAwpSeasonId.objects.get(
            start_date__lte=now, end_date__gte=now)
        players = RankAwpSeason.objects.filter(
            season_id=season.season_id).order_by("-score")[:3]
        preparedPlayers, topAvatarUrl = preparePlayers(players)
        sendDiscordMessage(preparedPlayers, topAvatarUrl)
        return
