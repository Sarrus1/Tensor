from django.db import models
from django.utils import timezone

class InternalStats(models.Model):
		total_users = models.IntegerField()
		days_played = models.IntegerField()
		total_bans = models.IntegerField()
		timestamp = models.DateTimeField(default=timezone.now)

		def __str__(self):
				return str(self.timestamp) if self.timestamp else ''

		class Meta:
				verbose_name_plural = "Internal Stats"