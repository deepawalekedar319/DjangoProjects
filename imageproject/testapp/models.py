from django.db import models

class Category(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.title


# create Image model

class Video(models.Model):
	video=models.FileField(upload_to='videos/%y',default='SOME STRING')
