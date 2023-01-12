from operator import truediv
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# class company_master(models.Model):
#     company_name = models.CharField(max_length=2000)
#     BIN_number = models.CharField(max_length=30)
#     industry = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     created_by = models.CharField(max_length=100)

#     class Meta:
#         unique_together = ("BIN_number", "country")
        
#     def __str__(self):
#         return self.company_name


# class role_master(models.Model):
#     role_name = models.CharField(max_length=2000)
    # company = models.ForeignKey(company_master, on_delete=CASCADE, null=True)

    # def __str__(self):
    #     return self.role_name

# class UserType(models.Model):
#     name = models.CharField(max_length=250,null = True, blank=True)
#     def __str__(self):
#         return self.name

class VehicleType(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser): 
    is_set_new_password = models.BooleanField(default=False)
   
    # company = models.ForeignKey(company_master, on_delete=CASCADE, null=True)
    username = models.CharField(unique=True,max_length=255,null = True, blank=True)
    #user_type = models.ForeignKey(UserType,on_delete=CASCADE,null = True, blank=True)
    phone = models.CharField(max_length=100,null = True, blank=True)
    auto_enable =models.BooleanField(default=False)
    time_intervial = models.CharField(max_length=20, help_text="input in second format", null=True, blank=True)
    vehicle_type = models.ForeignKey(VehicleType,on_delete=CASCADE, null=True, blank=True)
   

    def __str__(self):
        return self.email


class UserToken(models.Model):
    user_id = models.IntegerField(null=True)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()


class Reset(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)