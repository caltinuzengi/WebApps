from django.contrib import admin
from . models import Category, Media

class MediaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Category)
admin.site.register(Media, MediaAdmin)