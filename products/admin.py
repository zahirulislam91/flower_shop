from django.contrib import admin

# Register your models here.
from .models import Products



class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']
    
       
    def title(self,obj):
        return obj.user.title
    
    def price(self,obj):
        return obj.user.price


# Register your models here.
admin.site.register(Products,AdminProduct)
