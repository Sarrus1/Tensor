from django.db import models

class ApplicationModel(models.Model):
		Server = models.CharField(max_length=100)
		Email = models.EmailField()
		Discord = models.CharField(max_length=100)
		Age = models.IntegerField()
		Experience = models.CharField(max_length=100)
		Experience_more = models.TextField()
		Reason = models.TextField()
		SteamID = models.CharField(max_length=30)
		Name = models.CharField(max_length=30)
		Date = models.DateTimeField(auto_now_add=True)
		Status = models.CharField(max_length=100, default='Pending')

		def __str__(self):
				return str(self.Name) if self.Name else ''
		
		class Meta:
				verbose_name_plural = "Moderator Applications"


class ApplicationCommentsModel(models.Model):
		Application = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
		Admin = models.CharField(max_length=50)
		Comment = models.TextField()
		Vote = models.BooleanField(blank=True, null=True)

		def __str__(self):
				return str(self.Name) if self.Name else ''
		
		class Meta:
				verbose_name_plural = "Moderator Applications"