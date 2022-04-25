from django.contrib import admin

from .models import delo, Type

class deloAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time', 'importance', 'type')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)
admin.site.register(delo, deloAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Type, TypeAdmin)

# Register your models here.
