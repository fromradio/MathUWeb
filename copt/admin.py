from django.contrib import admin
from copt.models import Chapter,Item,Introduction

class IntroductionInline(admin.TabularInline):
	model = Introduction
class ItemInline(admin.TabularInline):
	model = Item
	extra = 3
class ChapterAdmin(admin.ModelAdmin):
	fieldsets =[
		(None, 		{'fields':['name']}),
	]
	inlines = [IntroductionInline,ItemInline]
admin.site.register(Chapter,ChapterAdmin)