from django.db import models
from django.utils import timezone

class Server(models.Model):
		name = models.CharField(max_length=100)
		ip = models.CharField(max_length=50)
		port = models.IntegerField()
		user = models.CharField(max_length=50)
		instance_name = models.CharField(max_length=50)
		sshport = models.IntegerField(default=12345)

		def __str__(self):
				return str(self.name) if self.name else ''
		
		@property
		def connectionInfo(self):
				return "{}:{}".format(self.ip, self.port)

		class Meta:
				verbose_name_plural = "Servers"


class PlayerCount(models.Model):
		timestamp = models.DateTimeField(default=timezone.now)
		player_count = models.IntegerField()
		max_player = models.IntegerField()
		server = models.ForeignKey(Server, related_name='playercount', on_delete=models.CASCADE)
		isdown = models.BooleanField(default=False)
		current_map = models.CharField(max_length=150, default="")

		def __str__(self):
				return str(self.server) if self.server else ''


class ServerControlModel(models.Model):
		timestamp = models.DateTimeField(default=timezone.now)
		uuid = models.CharField(max_length=100)
		output = models.TextField()
		status = models.IntegerField(default=-1)