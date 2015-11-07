from django.contrib import admin

# Register your models here.
from .models import Presentation


class PresentationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Presentation, PresentationAdmin)
