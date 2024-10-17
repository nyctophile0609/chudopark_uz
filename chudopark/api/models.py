from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import datetime
import os
import shutil
from chudopark.settings import MEDIA_ROOT 

ADMIN_USER_STATUS_CHOICES =[("high_rank","High"),('middle_rank', 'Middle'),('low_rank', 'Low'),]

class UserModel(AbstractUser):
    admin_status= models.CharField(choices=ADMIN_USER_STATUS_CHOICES,max_length=20)
    telegram_id=models.CharField(max_length=20,null=True)
    telegram_username=models.CharField(max_length=100,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    

class CategoryModel(models.Model):
    name=models.CharField(max_length=150,)
    created_date=models.DateTimeField(auto_now_add=True)

 

class ProductModel(models.Model):
    name=models.CharField(max_length=250)
    category=models.ForeignKey(CategoryModel,on_delete=models.SET_NULL,null=True)
    price=models.DecimalField(max_digits=32, decimal_places=2)
    height=models.CharField(max_length=250)
    width=models.CharField(max_length=250)
    length=models.CharField(max_length=250)
    material=models.CharField(max_length=250)
    color=models.CharField(max_length=250)
    build_time=models.CharField(max_length=100)
    builder=models.CharField(max_length=250)
    product_image=models.ImageField()
    created_date=models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image_instance = self.product_image
        new_directory_path = os.path.join(MEDIA_ROOT, f"product/product_{self.id}")
        if not os.path.exists(new_directory_path):
            os.makedirs(new_directory_path)
        source_image_path = image_instance.path
        _, file_name = os.path.split(source_image_path)
        new_image_path = os.path.join(new_directory_path, file_name)
        try:
            shutil.move(source_image_path, new_image_path)
        except Exception as e:
             return False
        if self.product_image!=f"product/product_{self.id}/{file_name}":
            self.product_image = f"product/product_{self.id}/{file_name}"
            self.save()
    class Meta:
            ordering = ['-created_date']

class ProductSubsetModel(models.Model):
    name=models.CharField(max_length=250)
    category=models.ForeignKey(CategoryModel,on_delete=models.SET_NULL,null=True)
    products=models.ManyToManyField(ProductModel,blank=True,)
    price=models.DecimalField(max_digits=32, decimal_places=2)
    height=models.CharField(max_length=250)
    width=models.CharField(max_length=250)
    subset_image=models.ImageField()
    created_date=models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image_instance = self.subset_image
        new_directory_path = os.path.join(MEDIA_ROOT, f"psubsets/product_{self.id}")
        if not os.path.exists(new_directory_path):
            os.makedirs(new_directory_path)
        source_image_path = image_instance.path
        _, file_name = os.path.split(source_image_path)
        new_image_path = os.path.join(new_directory_path, file_name)
        try:
            shutil.move(source_image_path, new_image_path)
        except Exception as e:
             return False
        if self.subset_image!=f"psubsets/product_{self.id}/{file_name}":
            self.subset_image = f"psubsets/product_{self.id}/{file_name}"
            self.save()
    class Meta:
            ordering = ['-created_date']

class ApplicationModel(models.Model):
    name=models.CharField(max_length=100)
    number1=models.CharField(max_length=25)
    number2=models.CharField(max_length=25,null=True)
    products=models.ManyToManyField(ProductModel,blank=True)
    product_sets=models.ManyToManyField(ProductSubsetModel,blank=True)
    description=models.TextField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    
class DiscountModel(models.Model):
    product=models.ManyToManyField(ProductModel,blank=True)
    productsubset=models.ManyToManyField(ProductSubsetModel,blank=True)
    discount=models.DecimalField(max_digits=5,decimal_places=2)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    created_date=models.DateTimeField(auto_now_add=True)

