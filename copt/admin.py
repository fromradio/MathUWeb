from django.contrib import admin
from copt.models import Chapter,Item,Introduction

class IntroductionInline(admin.TabularInline):
	model = Introduction
class ItemInline(admin.TabularInline):
	model = Item
	extra = 3
class ChapterAdmin(admin.ModelAdmin):
	list_display = ['name','related_project']
	fieldsets =[
		(None, 		{'fields':['name']}),
		('Project', {'fields':['project']})
	]
	inlines = [IntroductionInline,ItemInline]
	def related_project(self,obj):
		return '%s'%(obj.project.title)
admin.site.register(Chapter,ChapterAdmin)