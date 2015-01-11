from django.db import models
from home.models import Project

def get_project():
	return Project.objects.get(title="COPT")

class Content(models.Model):
	title = models.CharField(max_length=200)
	def __unicode__(self):
		return self.title

class Chapter(models.Model):
	project = models.ForeignKey(Project,default=get_project)
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Introduction(models.Model):
	chapter = models.ForeignKey(Chapter)
	content = models.CharField(max_length=5000)
	def __unicode__(self):
		return "introduction"

class Item(models.Model):
	chapter = models.ForeignKey(Chapter)
	name = models.CharField(max_length=500)
	description = models.CharField(max_length=1000)
	def __unicode__(self):
		return self.name