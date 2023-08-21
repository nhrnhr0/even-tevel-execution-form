from django.db import models

# Create your models here.
class ProductExtra(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='product_extras')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Product Extras'