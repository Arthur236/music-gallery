from django.contrib import admin
from . models import Album, Song

# Add album table to the admin interface
admin.site.register(Album)
admin.site.register(Song)
