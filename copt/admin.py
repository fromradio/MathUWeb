from django.contrib import admin
from copt.models import Chapter,Item

class ItemInline(admin.TabularInline):
	model = Item
	extra = 3
class ChapterAdmin(admin.ModelAdmin):
	fieldsets =[
		(None, 		{'fields':['name']}),
	]
	inlines = [ItemInline]
admin.site.register(Chapter,ChapterAdmin)