from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from notes.models import *

# Register your models here.


class NotesMediaAdmin(admin.ModelAdmin):
    list_display = ("file_name", "notes_id", "file_size")


class NotesLinkAdmin(admin.ModelAdmin):
    list_display = ("n_link", "n_link_about", "n_link_id")


admin.site.register(NotesMedia, NotesMediaAdmin)
admin.site.register(NotesLink, NotesLinkAdmin)
