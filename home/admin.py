from django.contrib import admin
from home.models import Project
from copt.models import Chapter

class ChapterInline(admin.TabularInline):
	model = Chapter
	extra = 3

class ProjectAdmin(admin.ModelAdmin):
	fieldsets =[
		(None, 		{'fields':['title']}),
	]
	inlines = [ChapterInline]
admin.site.register(Project,ProjectAdmin)
