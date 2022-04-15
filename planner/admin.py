from django.contrib import admin

from .models import delo

class deloAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time', 'importance')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)
admin.site.register(delo, deloAdmin)

# Register your models here.
