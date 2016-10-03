from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, FormView
from gscan.models import *
from gscan.tasks.tasks import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User

import hashlib
import time

@login_required(login_url="/")
def scan_index(request):
	task_list = Tasks.objects.all()
	return render(request, 'index.html' ,{'task_list' : task_list})

@login_required(login_url="/")
def scan_task(request):
	if request.method == 'POST':
		taskname = request.POST.get('taskname')
		target = request.POST.get('target')
		config = request.POST.get('config')
		taskid = hashlib.md5(str(time.time())).hexdigest()[0:20]
		new_task = Tasks(
					taskid = taskid,
					taskname = taskname,
					target = target,
					domain = 'pend',
					service = 'pend',
					weakfile = 'pend',
					status = 'start',
					config = config,
					)
		new_task.save()
		manage_task.delay(taskid)
		return HttpResponseRedirect('/index')
	config_list = Config.objects.all()
	return render(request, 'tasks.html', {'config_list': config_list})

@login_required(login_url="/")
def scan_login(request):
	return render(request, 'login.html')

@login_required(login_url="/")
def scan_plugin(request):
	plugin_list = Plugins.objects.all()
	return render(request, 'plugin.html',{'plugin_list' : plugin_list})


@login_required(login_url="/")
def domain_info(request, task_id):
	domain_list = Domain.objects.filter(taskid=task_id).order_by('ip')
	return render(request, 'domaininfo.html' ,{'domain_list' : domain_list, 'task_id' : task_id})

@login_required(login_url="/")
def service_info(request, task_id):
	service_list = Service.objects.filter(taskid=task_id).order_by('ip','port')
	return render(request, 'serviceinfo.html' ,{'service_list' : service_list, 'task_id' : task_id})

@login_required(login_url="/")
def file_info(request, task_id):
	weakfile_list = Weakfile.objects.filter(taskid=task_id)
	return render(request, 'fileinfo.html' ,{'weakfile_list' : weakfile_list, 'task_id' : task_id})


@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url="/")
def scan_config(request):
	config_list = Config.objects.all()
	return render(request, 'config.html', {'config_list' : config_list})


@login_required(login_url="/")
def config_add(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		ports = request.POST.get('ports')
		description = request.POST.get('description')
		new_config = Config(
					name = name,
					ports = ports,
					description = description,
					)
		new_config.save()
		return HttpResponseRedirect("/config")
	return render(request, 'cadd.html')



@login_required(login_url="/")
def config_edit(request, id):
	if request.method == 'POST':
		ports = request.POST.get('ports')
		description = request.POST.get('description')
		Config.objects.filter(id = id).update(ports=ports,description=description)
		config_list = Config.objects.all()
		return render(request, 'config.html', {'config_list' : config_list})
	config_rs = Config.objects.filter(id=id).all()
	return render(request, 'cedit.html', {'config_rs' : config_rs})

@login_required(login_url="/")
def scan_profile(request):
	user = User.objects.get(id = 1)
	return render(request, 'profile.html', {'user' : user})


def celery_test(request):
	taskid = '5d16a5715682a70f2ea3'
	manage_task.delay(taskid)
	return render(request, 'login.html')


