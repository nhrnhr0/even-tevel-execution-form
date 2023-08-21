from django.contrib import admin
from .models import WeightDepthRatio


# Register your models here.
class WeightDepthRatioAdmin(admin.ModelAdmin):
    list_display = ['weight', 'depth']
    search_fields = ['weight', 'depth']
admin.site.register(WeightDepthRatio, WeightDepthRatioAdmin)