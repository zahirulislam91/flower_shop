from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from category.models import Category
from . import serializers
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']