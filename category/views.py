from django.shortcuts import render

# Create your views here.
from category.models import Category
from . import serializers
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer