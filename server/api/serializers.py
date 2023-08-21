
from category.models import Category
from rest_framework import serializers
from subcategory.models import subcategory
from weights.models import WeightDepthRatio

class SubcategoryChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = subcategory
        fields = ('id', 'title', 'image',)
        
class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategoryChildSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'subcategories')


class WeightDepthRatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightDepthRatio
        fields = ('id', 'weight', 'depth',)