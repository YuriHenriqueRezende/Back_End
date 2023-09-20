from django.contrib import admin
from .models import *
# Register your models here.


class detCharacter(admin.ModelAdmin):
    list_display = ('id', 'name', 'species')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10


# registra as configurações realizadas do model na página de admin
admin.site.register(Character, detCharacter)


class detLocation(admin.ModelAdmin):
    list_display = ('id', 'name', 'dimension')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10


# registra as configurações realizadas do model na página de admin
admin.site.register(Location, detLocation)


class detEpisode(admin.ModelAdmin):
    list_display = ('id', 'name', 'Episode')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10


# registra as configurações realizadas do model na página de admin
admin.site.register(Episode, detEpisode)
