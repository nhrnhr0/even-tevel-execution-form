from django.contrib import admin
from .models import Category
from django.utils.html import mark_safe
from django.conf import settings

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_display']
    search_fields = ['title']
    
    def image_display(self, obj):
        return mark_safe('<img src="%s" width="100" />' % obj.image.url)
admin.site.register(Category, CategoryAdmin)