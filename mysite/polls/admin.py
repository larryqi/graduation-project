from django.contrib import admin

# Register your models here.
from .models import Server

class ServerAdmin(admin.ModelAdmin):
	list_display = ('server_name','server_ip','server_teacher')
	list_filter = ['server_teacher']
	search_fields = ['server_name']

admin.site.register(Server,ServerAdmin)
