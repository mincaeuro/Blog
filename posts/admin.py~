from django.contrib import admin

from .models import Komentar, Prispevok


class KomentPodPrispevkom(admin.StackedInline):
    model = Komentar
    extra = 0

class PrispevokAdm(admin.ModelAdmin):
	#list_display = ('title', 'pub_date','user', 'was_published_recently')
	fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['text']}),
        (None,               {'fields': ['image']}),
	(None,			{'fields': ['user']}),
        (None,			 {'fields': ['pub_date']}),
	]
	inlines = [KomentPodPrispevkom]
    #list_filter = ['pub_date']
    #search_fields = ['title']
	

class KomentAdm(admin.ModelAdmin):
	list_display = ('text', 'pub_date','user', 'was_published_recently', 'postRef')
	list_filter = ['pub_date']
	search_fields = ['text']
	

admin.site.register(Prispevok, PrispevokAdm)
admin.site.register(Komentar, KomentAdm)
