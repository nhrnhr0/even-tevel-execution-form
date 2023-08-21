from django.contrib import admin
from .models import ProductExtra
from django.utils.html import mark_safe
# Register your models here.
class ProductExtraAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_display']
    search_fields = ['title']
    
    def image_display(self, obj):
        return mark_safe('<img src="%s" width="100" />' % obj.image.url)
admin.site.register(ProductExtra, ProductExtraAdmin)