from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from solutions_page.models import *

# Register your models here.


class SolutionsMediaAdmin(admin.ModelAdmin):
    list_display = ("file_name", "solutions_id", "file_size")


class SolutionsLinkAdmin(admin.ModelAdmin):
    list_display = ("s_link", "s_link_about", "s_link_id")


admin.site.register(SolutionsMedia, SolutionsMediaAdmin)
admin.site.register(SolutionsLink, SolutionsLinkAdmin)
