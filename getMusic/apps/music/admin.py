from django.contrib import admin
from .models import Song, Playlist, Engine
# Register your models here.


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
   list_display = ["title", "engine"]
   search_fields = ["title", "artist", "lyrics"]


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
   list_display = ["title"]
   search_fields = ["title"]


admin.site.register(Engine)
