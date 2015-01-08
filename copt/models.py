from django.db import models

class Content(models.Model):
	title = models.CharField(max_length=200)
	def __unicode__(self):
		return self.title

class Chapter(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Item(models.Model):
	chapter = models.ForeignKey(Chapter)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	def __unicode__(self):
		return self.name