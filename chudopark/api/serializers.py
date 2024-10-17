from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class UserModelSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=UserModel
        fields=["id","username","admin_status","telegram_id","telegram_username","password"]
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance
    
class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model=CategoryModel
        fields="__all__"

class ProductModelSerializer(ModelSerializer):
    class Meta:
        model=ProductModel
        fields="__all__"
    
class ProductSubsetModelSerializer(ModelSerializer):
    class Meta:
        model=ProductSubsetModel
        fields="__all__"

class ApplicationModelSerializer(ModelSerializer):
    class Meta:
        model=ApplicationModel
        fields="__all__"

    
class DiscountModelSerializer(ModelSerializer):
    class Meta:
        model=DiscountModel
        fields="__all__"
    
