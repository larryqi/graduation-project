from django.db import models

# Create your models here.
class Server(models.Model):
	server_id = models.CharField(max_length=200)
	server_name = models.CharField(max_length=200)
	server_teacher = models.CharField(max_length=200)
	server_ip = models.GenericIPAddressField()
	server_url = models.URLField(max_length=200)
	def __unicode__(self):
		return self.server_name
