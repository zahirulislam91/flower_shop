from django.shortcuts import render

# Create your views here.

from order.models import Order
from . import serializers
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer