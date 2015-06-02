from django.contrib import admin

from .models import Komentar, Prispevok

# Register your models here.

#class KomentPodPrispevkom(admin.StackedInline):
#	model = Prispevok
#	extra = 3

#class KomentAdmin(admin.ModelAdmin):
#	fieldsets = [
#	(None, {'fields': ['text']}),
#	('Date info', {'fileds':['pub_date'], 'classes': ['collapse']}),
#	]
#	inlines = [KomentPodPrispevkom]


class PrispevokAdm(admin.ModelAdmin):
	list_display = ('title', 'pub_date','user', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['title']

class KomentAdm(admin.ModelAdmin):
	list_display = ('text', 'pub_date','user', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['text']
	

admin.site.register(Prispevok, PrispevokAdm)
admin.site.register(Komentar, KomentAdm)
