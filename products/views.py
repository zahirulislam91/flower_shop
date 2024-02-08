from django.shortcuts import render

# Create your views here.

from order.models import Products
from . import serializers
from rest_framework import viewsets
from rest_framework import pagination


class ProductPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = ProductPagination