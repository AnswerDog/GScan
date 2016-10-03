from __future__ import unicode_literals

from django.db import models


class Tasks(models.Model):
	taskid = models.CharField(max_length=50)
	taskname = models.TextField()
	target = models.TextField()
	domain = models.CharField(max_length=5)
	service = models.CharField(max_length=5)
	weakfile = models.CharField(max_length=5)
	status = models.CharField(max_length=5)
	starttime = models.DateField(auto_now=True)
	endtime = models.DateField(null=True)
	config = models.IntegerField()

	def __unicode__(self):
		return self.target

class Plugins(models.Model):
	name = models.TextField()
	type = models.TextField()
	path = models.TextField()
	description = models.TextField()
	port = models.TextField()

	def __unicode__(self):
		return self.name
		
class Domain(models.Model):
	taskid = models.CharField(max_length=20)
	target = models.TextField()
	ip = models.TextField()
	status = models.CharField(max_length=20)

	def __unicode__(self):
		return self.target
		
		
class Service(models.Model):
	taskid = models.CharField(max_length=20)
	target = models.TextField()
	ip = models.TextField()
	port = models.CharField(max_length=10)
	pluginpath = models.CharField(max_length=100)
	status = models.CharField(max_length=20)
	data = models.CharField(max_length=100)

	def __unicode__(self):
		return self.target


class Weakfile(models.Model):
	taskid = models.CharField(max_length=20)
	target = models.TextField()
	weakfile = models.TextField()
	plugid = models.IntegerField()
	status = models.CharField(max_length=20)
	data = models.CharField(max_length=100)
	pluginpath = models.CharField(max_length=100)

	def __unicode__(self):
		return self.target


class MasTmp(models.Model):
	taskid = models.CharField(max_length=20)
	ip = models.TextField()
	status = models.CharField(max_length=20)

	def __unicode__(self):
		return self.ip


class Config(models.Model):
	name = models.TextField()
	ports = models.TextField()
	description = models.TextField()
	createtime = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.name


