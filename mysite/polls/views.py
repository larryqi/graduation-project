from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from data import get_data
from polls.models import Server
import random
# Create your views here.

@login_required
def index(request):
	if(random.randint(0,10)<3):
		server_id,server_name,server_teacher,server_ip,server_url=get_data()
		Server.objects.all().delete()
		for i in range(len(server_id)):
			s = Server(server_id=server_id[i],server_name=server_name[i],server_teacher=server_teacher[i],server_ip=server_ip[i],server_url=server_url[i])
			s.save()	
	server_list = Server.objects.filter(server_name__contains=request.user.username)
	context = {'server_list':server_list,'user':request.user}
	return render(request, 'polls/index.html' ,context)
