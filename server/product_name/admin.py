from django.contrib import admin
from .models import CachedProductName
# Register your models here.
class CachedProductNameAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
admin.site.register(CachedProductName, CachedProductNameAdmin)
