from django.contrib import admin
from .models import Order
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'price', 'status']

    def product(self, obj):
        return obj.product.title

    def customer(self, obj):
        return obj.customer.first_name 

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.status == "Completed":
            email_subject = "Your Online Order is Completed"
            email_body = render_to_string('admin_email.html', {'user': obj.customer, 'product': obj.product})
            email = EmailMultiAlternatives(email_subject, '', to=[obj.customer.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

admin.site.register(Order, AdminOrder)






# from django.contrib import admin
# from .models import Order
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# class AdminOrder(admin.ModelAdmin):
#     list_display = ['product', 'customer', 'quantity', 'price', 'status']

#     def product(self, obj):
#         return obj.product

#     def customer(self, obj):
#         return obj.customer

#     def save_model(self, request, obj, form, change):
#         obj.save()
#         if obj.status == "Completed":
#             email_subject = "Your Online Order is Completed"
#             email_body = render_to_string('admin_email.html', {'user': obj.customer.user, 'product': obj.product})
#             email = EmailMultiAlternatives(email_subject, '', to=[obj.customer.user.email])
#             email.attach_alternative(email_body, "text/html")
#             email.send()

# admin.site.register(Order, AdminOrder)





# from django.contrib import admin

# from .models import Order
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# class AdminOder(admin.ModelAdmin):
#     list_display = ['product', 'customer','quantity', 'price', 'status']
    
       
#     def product(self,obj):
#         return obj.products.user.product
#     def customer(self,obj):
#         return obj.customer.user.customer
    
#     def save_model(self, request, obj, form, change):
#         obj.save()
#         if obj.status == "Completed":
#             email_subject = "Your Online Order is Completed"
#             email_body = render_to_string('admin_email.html', {'user' : obj.customer.user, 'product' : obj.product})
            
#             email = EmailMultiAlternatives(email_subject , '', to=[obj.customer.user.email])
#             email.attach_alternative(email_body, "text/html")
#             email.send()
    
    
# admin.site.register(Order, AdminOder)


# from django.contrib import admin

# # Register your models here.
# from .models import Products



# class AdminProduct(admin.ModelAdmin):
#     list_display = ['name', 'price', 'category']


# # Register your models here.
# admin.site.register(Products,AdminProduct)