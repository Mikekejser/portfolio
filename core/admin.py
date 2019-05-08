from django.contrib import admin
from .models import Site, Contact


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
	list_display = ('sitename',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('navn', 'email')