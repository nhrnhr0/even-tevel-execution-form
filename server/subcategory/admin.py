from django.contrib import admin
from .models import subcategory
from django.utils.html import mark_safe
# Register your models here.
class subcategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_display', 'category']
    search_fields = ['title']
    
    def image_display(self, obj):
        return mark_safe('<img src="%s" width="100" />' % obj.image.url)
admin.site.register(subcategory, subcategoryAdmin)