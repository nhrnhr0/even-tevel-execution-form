from django.db import models

# Create your models here.
class subcategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory')
    category = models.ForeignKey('category.category', on_delete=models.CASCADE, related_name='subcategories')
    def __str__(self):
        return self.title