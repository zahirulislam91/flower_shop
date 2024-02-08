from django.db import models

# Create your models here.
from products.models import Products
from customer.models import Customer
import datetime



ORDER_STATUS = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
]


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.CharField (choices = ORDER_STATUS, max_length = 10, default="Pending")

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    def __str__(self):
        return f"Product : {self.product.title} , Customer : {self.customer.first_name}"
        
    