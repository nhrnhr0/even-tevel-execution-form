from django.db import models

# Create your models here.
class WeightDepthRatio(models.Model):
    weight = models.FloatField()
    depth = models.FloatField()
    
    def __str__(self):
        return str(self.weight) + ' ' + str(self.depth)
    
    class Meta:
        unique_together = ('weight', 'depth')