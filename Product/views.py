from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework import generics
# for add or remove data


class BrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class ProductOneViewset(viewsets.ModelViewSet):
    queryset = ProductNumberOne.objects.all().order_by('name')
    serializer_class = ProductNumberOneSerializer


class ProductTwoViewset(viewsets.ModelViewSet):
    queryset = ProductNumberTwo.objects.all().order_by('name')
    serializer_class = ProductNumbertwoSerializer


class ProductThreeViewset(viewsets.ModelViewSet):
    queryset = ProductNumberThree.objects.all().order_by('name')
    serializer_class = ProductNumberthreeSerializer


# for show brand and category
class ProductOneAsked(generics.ListAPIView):
    serializer_class = ProductNumberOneSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return ProductNumberOne.objects.filter(Q(category__name=name) |
                                               Q(brand__name=name)).filter(numbers__gte=10)


class ProducttwoAsked(generics.ListAPIView):
    serializer_class = ProductNumbertwoSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return ProductNumberTwo.objects.filter(Q(category__name=name) |
                                               Q(brand__name=name)).filter(numbers__gte=10)


class ProductthreeAsked(generics.ListAPIView):
    serializer_class = ProductNumberOneSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return ProductNumberThree.objects.filter(Q(category__name=name) |
                                               Q(brand__name=name)).filter(numbers__gte=10)
