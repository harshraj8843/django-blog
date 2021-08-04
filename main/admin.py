from django.contrib import admin

from . import models

# Register your models here.

# blog admin
@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "date")
    search_fields = ("id", "title", "author", "date")

# contact admin
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "message", "time")
    search_fields = ("id", "name", "email", "message", "time")