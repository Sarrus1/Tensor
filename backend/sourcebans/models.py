from django.db import models
from datetime import datetime
from steam.steamid import SteamID
from django.apps import apps
from django.utils.safestring import mark_safe
from django.utils.timezone import localtime
from time import mktime
from time import *
from servers.models import Server


class SbGroups(models.Model):
		gid = models.AutoField(primary_key=True)
		type = models.SmallIntegerField()
		name = models.CharField(max_length=128)
		flags = models.IntegerField()

		class Meta:
				managed = False
				db_table = 'sb_groups'


class SbAdmins(models.Model):
		aid = models.AutoField(primary_key=True)
		user = models.CharField(unique=True, max_length=64)
		authid = models.CharField(max_length=64)
		password = models.CharField(max_length=128)
		gid = models.ForeignKey(SbGroups, on_delete=models.DO_NOTHING, db_column="gid")
		email = models.CharField(max_length=128)
		validate = models.CharField(max_length=128, blank=True, null=True)
		extraflags = models.IntegerField()
		immunity = models.IntegerField()
		srv_group = models.CharField(max_length=128, blank=True, null=True)
		srv_flags = models.CharField(max_length=64, blank=True, null=True)
		srv_password = models.CharField(max_length=128, blank=True, null=True)
		lastvisit = models.IntegerField(blank=True, null=True)

		def steamid64(self):
				return SteamID(self.authid).as_64

		class Meta:
				managed = False
				db_table = 'sb_admins'
				verbose_name_plural = "SB Admins"


class SbAdminsServersGroups(models.Model):
		admin_id = models.IntegerField()
		group_id = models.IntegerField()
		srv_group_id = models.IntegerField()
		server_id = models.IntegerField()

		class Meta:
				managed = False
				db_table = 'sb_admins_servers_groups'


class SbServers(models.Model):
		sid = models.AutoField(primary_key=True)
		ip = models.CharField(max_length=64)
		port = models.IntegerField()
		rcon = models.CharField(max_length=64)
		modid = models.IntegerField()
		enabled = models.IntegerField()

		class Meta:
				managed = False
				db_table = 'sb_servers'
				unique_together = (('ip', 'port'),)
				verbose_name_plural = "SB Servers"
		
		def __str__(self):
				server = Server.objects.filter(port=self.port).first()
				return server.name if server is not None else "Unknown"
		

class SbBans(models.Model):
		bid = models.AutoField(primary_key=True)
		ip = models.CharField(max_length=32, blank=True, null=True)
		authid = models.CharField(max_length=64)
		name = models.CharField(max_length=128)
		created = models.IntegerField()
		ends = models.IntegerField()
		length = models.IntegerField()
		reason = models.TextField()
		aid = models.IntegerField()
		adminip = models.CharField(db_column='adminIp', max_length=32)  # Field name made lowercase.
		sid = models.ForeignKey(SbServers, on_delete=models.DO_NOTHING, db_column="sid")
		country = models.CharField(max_length=4, blank=True, null=True)
		removedby = models.IntegerField(db_column='RemovedBy', blank=True, null=True)  # Field name made lowercase.
		removetype = models.CharField(db_column='RemoveType', max_length=3, blank=True, null=True)  # Field name made lowercase.
		removedon = models.IntegerField(db_column='RemovedOn', blank=True, null=True)  # Field name made lowercase.
		type = models.IntegerField()
		ureason = models.TextField(blank=True, null=True)

		@property
		def date_start(self):
				return datetime.fromtimestamp(self.created).strftime('%d.%m.%Y-%H:%M')
		
		@property
		def date_end(self):
				return datetime.fromtimestamp(self.ends).strftime('%d.%m.%Y-%H:%M')

		@property
		def admin_authid(self):
				if self.aid == 0:
						return 0
				return SbAdmins.objects.get(aid=self.aid).authid

		@property
		def admin_name(self):
				SteamUser = apps.get_model('authentication.SteamUser')
				if self.aid == 0:
					return "CONSOLE"
				admin = SbAdmins.objects.get(aid=self.aid)
				username = admin.user
				steamid = admin.steamid64()
				admin = SteamUser.objects.get(steamid=steamid)
				if admin:
					return admin.personaname
				return username
		
		@property
		def percent(self):
				start = self.created
				end = self.ends
				now = int(datetime.now().timestamp())
				if now>=end:
					percent = 100
				elif start>=end or start>now:
					percent = 0
				else:
					percent = round(((start-now)/(start-end)), 2)*100
				if self.length == 0:
					progress_bar_class = "danger"
				elif percent < 100:
					progress_bar_class = "warning"
				else:
					progress_bar_class = "success"
				return {"percent":percent, "progress_bar_class":progress_bar_class}
		
		@property
		def ban_length(self):
				length = self.length
				if length == 0:
						length = "Permanent"
				elif length < 3600:
						length = strftime('%Mmin', gmtime(length))
				elif length <= 84600:
						length = strftime('%Hhr', gmtime(length))
				else:
						length = str(length//84600) + "d"
				return length

		@property
		def duration(self):
				length = self.length
				end = self.ends
				now = int(datetime.now().timestamp())
				if now>=end and length!=0 :
					status = "(Expired)"
					badge = "success"
				elif length==0:
					status = "Permanent"
					badge = "danger"
				else:
					status = "(In Progress)"
					badge = "warning"
				length = self.ban_length if self.ban_length != "Permanent" else ""
				
				return mark_safe("<span class='badge badge-{}' style='text-aligne:center'>{} {}</span>".format(badge, length, status))

		@property
		def steam64(self):
				return SteamID(self.authid).as_64

		@property
		def steam3(self):
				return SteamID(self.authid).as_steam3

		@property
		def totalBans(self):
				return SbBans.objects.filter(authid=self.authid).count()
		
		@property
		def blocked(self):
				return SbBanlog.objects.filter(bid=self.bid)

		class Meta:
				managed = False
				db_table = 'sb_bans'
				app_label = 'sourcebans'


class SbBanlog(models.Model):
		sid = models.ForeignKey(SbServers, on_delete=models.DO_NOTHING, db_column="sid")
		time = models.IntegerField(primary_key=True)
		name = models.CharField(max_length=128)
		bid = models.ForeignKey(SbBans, on_delete=models.CASCADE, db_column='bid')

		class Meta:
				managed = False
				db_table = 'sb_banlog'
				unique_together = (('sid', 'time', 'bid'),)
		
		def __str__(self):
				return self.name


class SbComments(models.Model):
		cid = models.AutoField(primary_key=True)
		bid = models.IntegerField()
		type = models.CharField(max_length=1)
		aid = models.IntegerField()
		commenttxt = models.TextField()
		added = models.IntegerField()
		editaid = models.IntegerField(blank=True, null=True)
		edittime = models.IntegerField(blank=True, null=True)

		class Meta:
				managed = False
				db_table = 'sb_comments'


class SbComms(models.Model):
		bid = models.AutoField(primary_key=True)
		authid = models.CharField(max_length=64)
		name = models.CharField(max_length=128)
		created = models.IntegerField()
		ends = models.IntegerField()
		length = models.IntegerField()
		reason = models.TextField()
		aid = models.IntegerField()
		adminip = models.CharField(db_column='adminIp', max_length=32)  # Field name made lowercase.
		sid = models.IntegerField()
		removedby = models.IntegerField(db_column='RemovedBy', blank=True, null=True)  # Field name made lowercase.
		removetype = models.CharField(db_column='RemoveType', max_length=3, blank=True, null=True)  # Field name made lowercase.
		removedon = models.IntegerField(db_column='RemovedOn', blank=True, null=True)  # Field name made lowercase.
		type = models.IntegerField()
		ureason = models.TextField(blank=True, null=True)

		class Meta:
				managed = False
				db_table = 'sb_comms'


class SbDemos(models.Model):
		demid = models.IntegerField(primary_key=True)
		demtype = models.CharField(max_length=1)
		filename = models.CharField(max_length=128)
		origname = models.CharField(max_length=128)

		class Meta:
				managed = False
				db_table = 'sb_demos'
				unique_together = (('demid', 'demtype'),)


class SbLog(models.Model):
		lid = models.AutoField(primary_key=True)
		type = models.CharField(max_length=1)
		title = models.CharField(max_length=512)
		message = models.TextField()
		function = models.TextField()
		query = models.TextField()
		aid = models.IntegerField()
		host = models.TextField()
		created = models.IntegerField()

		class Meta:
				managed = False
				db_table = 'sb_log'


class SbMods(models.Model):
		mid = models.AutoField(primary_key=True)
		name = models.CharField(unique=True, max_length=128)
		icon = models.CharField(max_length=128)
		modfolder = models.CharField(unique=True, max_length=64)
		steam_universe = models.IntegerField()
		enabled = models.IntegerField()

		class Meta:
				managed = False
				db_table = 'sb_mods'


class SbOverrides(models.Model):
		type = models.CharField(max_length=7)
		name = models.CharField(max_length=32)
		flags = models.CharField(max_length=30)

		class Meta:
				managed = False
				db_table = 'sb_overrides'
				unique_together = (('type', 'name'),)


class SbProtests(models.Model):
		pid = models.AutoField(primary_key=True)
		bid = models.ForeignKey(SbBans, on_delete=models.CASCADE, db_column='bid')
		datesubmitted = models.IntegerField(default=mktime(localtime()))
		reason = models.TextField()
		email = models.CharField(max_length=128)
		archiv = models.IntegerField(blank=True, null=True, default=0)
		archivedby = models.IntegerField(blank=True, null=True)
		pip = models.CharField(max_length=64)

		class Meta:
				managed = False
				db_table = 'sb_protests'
				verbose_name_plural = "SB Protests"


class SbServersGroups(models.Model):
		server_id = models.IntegerField(primary_key=True)
		group_id = models.IntegerField()

		class Meta:
				managed = False
				db_table = 'sb_servers_groups'
				unique_together = (('server_id', 'group_id'),)


class SbSettings(models.Model):
		setting = models.CharField(unique=True, max_length=128)
		value = models.TextField()

		class Meta:
				managed = False
				db_table = 'sb_settings'


class SbSrvgroups(models.Model):
		flags = models.CharField(max_length=30)
		immunity = models.PositiveIntegerField()
		name = models.CharField(max_length=120)
		groups_immune = models.CharField(max_length=255)

		class Meta:
				managed = False
				db_table = 'sb_srvgroups'


class SbSrvgroupsOverrides(models.Model):
		group_id = models.PositiveSmallIntegerField()
		type = models.CharField(max_length=7)
		name = models.CharField(max_length=32)
		access = models.CharField(max_length=5)

		class Meta:
				managed = False
				db_table = 'sb_srvgroups_overrides'
				unique_together = (('group_id', 'type', 'name'),)


class SbSubmissions(models.Model):
		subid = models.AutoField(primary_key=True)
		submitted = models.IntegerField()
		modid = models.IntegerField(db_column='ModID')  # Field name made lowercase.
		steamid = models.CharField(db_column='SteamId', max_length=64)  # Field name made lowercase.
		name = models.CharField(max_length=128)
		email = models.CharField(max_length=128)
		reason = models.TextField()
		ip = models.CharField(max_length=64)
		subname = models.CharField(max_length=128, blank=True, null=True)
		sip = models.CharField(max_length=64, blank=True, null=True)
		archiv = models.IntegerField(blank=True, null=True)
		archivedby = models.IntegerField(blank=True, null=True)
		server = models.IntegerField(blank=True, null=True)

		class Meta:
				managed = False
				db_table = 'sb_submissions'
