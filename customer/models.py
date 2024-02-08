from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)


    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    
    
# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     image = models.ImageField(upload_to='patient/images/')
#     mobile_no = models.CharField(max_length = 12)
    
#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name}"