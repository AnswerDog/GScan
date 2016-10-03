"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from gscan.views import *

urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	url(r'^logout$', logout),
    url(r'^index$', scan_index),
	url(r'^tasks$', scan_task),
	url(r'^plugin$', scan_plugin),
	url(r'^config$', scan_config),
	url(r'^profile$', scan_profile),
	url(r'^cadd$', config_add),
	url(r'^cedit/(?P<id>\d+)$', config_edit),
	url(r'^task/(?P<task_id>\w+)$', domain_info),
	url(r'^task/domain/(?P<task_id>\w+)$', domain_info),
	url(r'^task/service/(?P<task_id>\w+)$', service_info),
	url(r'^task/file/(?P<task_id>\w+)$', file_info),
	url(r'^test$', celery_test),
]
