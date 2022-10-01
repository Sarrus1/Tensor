import a2s
from discord_webhook import DiscordWebhook, DiscordEmbed
import re
from servers.models import Server, PlayerCount
from django.core.management.base import BaseCommand
from os import getenv


def send_discord_announce(server, successful):
    webhook = DiscordWebhook(url=getenv("DISCORD_WEBHOOK_SERVER_STATUS"))
    if successful:
        title = 'Server is back online'
        description = "A server query was successful. The server might is back online."
        color = 786176
    else:
        title = 'Server query failed'
        description = "A server query failed. The server might be down."
        color = 16711680
    embed = DiscordEmbed(title=title,
                         description=description,
                         color=color,
                         url="https://data.tensor.fr/servers/")
    embed.add_embed_field(name='Server', value=server.name, inline=True)
    embed.add_embed_field(name='IP', value="{}:{}".format(
        server.ip, server.port), inline=True)
    webhook.add_embed(embed)
    webhook.execute()

# Fonction liée à un cronjob pour query la télémétrie des serveurs


def playercounter():
    labels = []
    number = []
    for server in Server.objects.all():
        address = (server.ip, server.port)
        attempts = 0
        isdown = True
        # Attempt to query the server 3 times maximum
        while attempts < 3 and isdown:
            try:
                query = a2s.info(address, timeout=5, encoding=None)
                playernumber = query.player_count
                maxplayer = query.max_players
                current_map = query.map_name.decode('utf-8')
                HasWorkshop = re.search("^workshop/[0-9]*/", current_map)
                servername = query.server_name.decode('utf-8')
                if HasWorkshop:
                    current_map = current_map.replace(HasWorkshop[0], "")
                isdown = False
                queryset = PlayerCount.objects.filter(
                    server=server).order_by("-id")
                if queryset and queryset[0].isdown:
                    try:
                        send_discord_announce(server, True)
                    except Exception as e:
                        continue
                attempts += 1
            except:
                attempts += 1
                continue

                # If the queries failed 3 times in a row, send a discord message
        if attempts == 3:
            playernumber = 0
            maxplayer = 64
            current_map = "de_mirage"
            isdown = True
            servername = ""
            # Discord webhook message
            # Check if the server was down before to avoid spam
            queryset = PlayerCount.objects.filter(
                server=server).order_by("-id")
            if not queryset:
                try:
                    send_discord_announce(server, False)
                except Exception as e:
                    continue
            else:
                if not queryset[0].isdown:
                    try:
                        send_discord_announce(server, False)
                    except Exception as e:
                        continue

        # Ajout des données dans la BDD de django, pour ne pas perdre les données en cas de redémarrage.
        serverstat = PlayerCount(player_count=playernumber,
                                 max_player=maxplayer, server=server, current_map=current_map, isdown=isdown)
        serverstat.save()
        if servername != "" and servername != server.name:
            server.name = servername
            server.save()
        Name_id = Server.objects.get(name=server.name)
        queryset = PlayerCount.objects.filter(server=Name_id)
        # Suppression des données les plus anciennes lorsqu'il y en a trop,
        # Pour garder uniquement une fenêtre de temps
        if queryset.count() >= 36:
            to_delete = PlayerCount.objects.values()[:1].get()
            PlayerCount.objects.filter(id=to_delete['id']).delete()


class Command(BaseCommand):
    help = 'Query the servers'

    def handle(self, *args, **options):
        playercounter()
