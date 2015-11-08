from django.contrib import admin
from reversion.admin import VersionAdmin
# Register your models here.
from .models import Presentation


class PresentationAdmin(VersionAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Presentation, PresentationAdmin)
