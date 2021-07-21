from django.db import models


class Tvip(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    playername = models.CharField(max_length=200)
    playerid = models.CharField(unique=True, max_length=20)
    enddate = models.DateTimeField()
    admin_playername = models.CharField(max_length=36)
    admin_playerid = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tVip'


class Donators(models.Model):
		SteamID = models.CharField(max_length=30)
		Name = models.CharField(max_length=100, null=True)
		amount = models.IntegerField()
		date = models.DateTimeField(auto_now_add=True)

		def __str__(self):
				return str(self.Name) if self.Name else ''
		
		class Meta:
				verbose_name_plural = "Donators"