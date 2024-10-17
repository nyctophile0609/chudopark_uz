from rest_framework import permissions
from .models import *
from django.shortcuts import get_object_or_404
 
class IsHighRank(permissions.BasePermission):
    def has_permission(self, request, view):
        if UserModel.objects.get(id=request.user.id):
            if request.user.admin_status=="high_rank":
                return True
        return False
    
class IsMiddleRank(permissions.BasePermission):
    def has_permission(self, request, view):
        if UserModel.objects.get(id=request.user.id):
            if request.user.admin_status in ["middle_rank","high_rank"]:
                return True
        return False
    
class IsLowRank(permissions.BasePermission):
    def has_permission(self, request, view):
        if UserModel.objects.get(id=request.user.id):
            if request.user.admin_status in ["high_rank","middle_rank","low_rank"]:
                return True
        return False
    
    
class CanUpdateProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if UserModel.objects.get(id=request.user.id):
            if request.user.admin_status=="high_rank":
                return True
            elif request.user==obj:
                return True
        return False
    
class CanNotBePerformed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False