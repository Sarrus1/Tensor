from django.contrib import admin
from .models import *
from .forms import *
import mysql.connector
from steam.steamid import SteamID
from steamwebapi.api import ISteamUser
from django.core.mail import send_mail

from os import getenv

steamuserinfo = ISteamUser(
    steam_api_key=getenv("STEAM_API_KEY"))
mail_accept_message = "Hello,<br><br>Thanks you for your interest in the server :D<br>I've made you a moderator, which will become effective by the next server restart (every day at 5 a.m), which means that  you can kick players by typing /kick in chat. You can also use /mute, /gag and /silence.<br><br>Make sure to join our discord and to tell me that you're a moderator once you join it so i can add you to the moderator group.<br>Discord Server adress:  discord.tensor.fr<br><br>Go to the login page of http://ban.tensor.fr and click on Forgot Password to activate your account.<br>This can take a while.<br><br>If you have any questions just send me an email or message me on Discord and I'll get back to you when I have the time.<br>Cheers,<br>Sarrus"


def AddToSourcebans(steamid, email, Type, server):
    mydb = mysql.connector.connect(
        host="192.168.1.107",
        user="sourceban",
        password=getenv("DB_AWP_PASS"),
        database="sourceban"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT MAX(aid) FROM sb_admins")
    myresult = mycursor.fetchall()
    aid = myresult[0][0] + 1
    mycursor.execute("SELECT aid FROM sb_admins WHERE authid=%s", (steamid,))
    myresult = mycursor.fetchall()
    steamid64 = SteamID(steamid).as_64
    usersummary = steamuserinfo.get_player_summaries(
        steamid64)['response']['players'][0]
    user = usersummary['personaname']
    user = user.encode('ascii', 'ignore').decode('ascii')
    user = user.replace(" ", "")
    authid = steamid
    # This is a password hash, not the actual password. The hash is completely random,
    # the corresponding password is unknown, not security risk here.
    password = "$2y$10$uHWR/vD2G9fKTFXDuZbEYOKniOGokaeEPPyHt6Al3YQrLHpgDmI6q"

    if Type == 'Moderators':
        gid = 5
        group_id = 2
    else:
        gid = 2
        group_id = 1

    email = email

    validate = None
    extraflags = 0
    immunity = 0
    srv_groups = Type
    srv_flags = None
    srv_password = None
    last_visit = None

    if server == 'awp':
        server_group = 1
    elif server == 'surf':
        server_group = 3
    else:
        server_group = 4
    if not (myresult):
        mycursor.execute("INSERT INTO `sb_admins` (`aid`, `user`, `authid`, `password`, `gid`, `email`, `validate`, `extraflags`, `immunity`, `srv_group`, `srv_flags`, `srv_password`, `lastvisit`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                         (aid, user, authid, password, gid, email, validate, extraflags, immunity, Type, srv_flags, srv_password, last_visit))
    else:
        aid = myresult[0][0]

    mycursor.execute(
        "SELECT admin_id FROM `sb_admins_servers_groups` WHERE admin_id=%s AND group_id=%s AND srv_group_id=%s", (aid, group_id, server_group))
    myresult = mycursor.fetchall()

    if not (myresult):
        mycursor.execute(
            "INSERT INTO `sb_admins_servers_groups` (`admin_id`, `group_id`, `srv_group_id`, `server_id`) VALUES (%s, %s, %s, '-1')", (aid, group_id, server_group))

    else:
        aid = myresult[0][0]
        mycursor.execute(
            "INSERT INTO `sb_admins_servers_groups` (`admin_id`, `group_id`, `srv_group_id`, `server_id`) VALUES (%s, %s, %s, '-1')", (aid, group_id, server_group))


def Accept(modeladmin, request, queryset):
    for application in queryset:
        if application.Status == 'Pending':
            application.Status = 'Accepted'
            application.save()
            send_mail(
                'Moderator application',
                '',
                'information@tensor.fr',
                [application.Email],
                fail_silently=False,
                html_message=mail_accept_message
            )
            AddToSourcebans(application.SteamID,  application.Email,
                            "Moderators", application.Server)


Accept.short_description = "Accept applications"


def Reject(modeladmin, request, queryset):
    for application in queryset:
        if application.Status == 'Pending':
            application.Status = 'Rejected'
            application.save()


Reject.short_description = "Reject applications"


class ApplicationModelAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Date', 'Status']
    ordering = ['Date', 'Status']
    actions = [Accept, Reject]


admin.site.register(ApplicationModel, ApplicationModelAdmin)
