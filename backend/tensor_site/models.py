from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField


class News(models.Model):
		title = models.CharField(max_length=100)
		content = MarkdownxField()
		date = models.DateField(default=timezone.now)

		def __str__(self):
				return self.title
		
		class Meta:
				verbose_name_plural = "News"


SERVER_CHOICES = [
		('awp', 'AWP'),
		('retakes', 'Retakes'),
		('surf', 'Surf'),
		]