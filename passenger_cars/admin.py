from django.contrib import admin
from .models import *

class AutoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'photo', 'time_create', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Auto, AutoAdmin)
admin.site.register(Category, CategoryAdmin)