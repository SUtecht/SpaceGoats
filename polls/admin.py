from polls.models import Poll
from demo.models import *
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['question']}),
		('Date information',	{'fields': ['pub_date'],'classes': ['collapse']}),
	]

admin.site.register(Poll, PollAdmin)
admin.site.register(Event)
admin.site.register(Character)
admin.site.register(Player)
admin.site.register(Article)