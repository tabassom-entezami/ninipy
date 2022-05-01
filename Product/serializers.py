from rest_framework import serializers
from .models import *


class ProductNumberOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNumberOne
        fields = "__all__"


class ProductNumbertwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNumberTwo
        fields = "__all__"


class ProductNumberthreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNumberThree
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
