from django.shortcuts import render

# Create your views here.


def category(request):
    from category.models import Category
    from .serializers import CategorySerializer
    from rest_framework import generics
    class CategoryList(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
    return CategoryList.as_view()(request)

def weights_ratio(request):
    from weights.models import WeightDepthRatio
    from .serializers import WeightDepthRatioSerializer
    from rest_framework import generics
    class WeightsRatioList(generics.ListCreateAPIView):
        queryset = WeightDepthRatio.objects.all()
        serializer_class = WeightDepthRatioSerializer
    return WeightsRatioList.as_view()(request)