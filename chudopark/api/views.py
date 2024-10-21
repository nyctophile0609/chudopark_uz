from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from django.http import JsonResponse
from rest_framework import viewsets, filters

# from django_filters.rest_framework import DjangoFilterBackend
# from .filters import *
from .permissions import *


class UserModelViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

    @action(detail=False, methods=["post"])
    def logout(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_permissions(self):
        if self.action in ["logout"]:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == "update":
            permission_classes = [permissions.IsAuthenticated,CanUpdateProfile]
        elif self.action == "create" or self.action == "destroy":
            permission_classes = [permissions.IsAuthenticated,IsHighRank]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class CategoryModelViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    
    def get_permissions(self):
        if self.action == "update":
            permission_classes = [permissions.IsAuthenticated,]
        elif self.action == "create" or self.action == "destroy":
            permission_classes = [permissions.IsAuthenticated,IsLowRank]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class ProductModelViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name', 'price', 'discountmodel__discount']
    
    
    def get_permissions(self):
        if self.action == "update":
            permission_classes = [permissions.IsAuthenticated,]
        elif self.action == "create" or self.action == "destroy":
            permission_classes = [permissions.IsAuthenticated,IsLowRank]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class ProductSubsetModelViewSet(ModelViewSet):
    queryset = ProductSubsetModel.objects.all()
    serializer_class = ProductSubsetModelSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name', 'price', 'discountmodel__discount']

    def get_permissions(self):
        if self.action == "update":
            permission_classes = [permissions.IsAuthenticated,]
        elif self.action == "create" or self.action == "destroy":
            permission_classes = [permissions.IsAuthenticated,IsLowRank]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class ApplicationModelViewSet(ModelViewSet):
    queryset=ApplicationModel.objects.all()
    serializer_class=ApplicationModelSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    def get_permissions(self):
        if self.action == "update":
            permission_classes = [permissions.IsAuthenticated,]
        elif self.action == "create" or self.action == "destroy":
            permission_classes = [permissions.IsAuthenticated,IsLowRank]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]



class DiscountModelViewSet(ModelViewSet):
    queryset=DiscountModel.objects.all()
    serializer_class=DiscountModelSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    def get_permissions(self):
        if self.action == "update":
            permission_classes = [permissions.IsAuthenticated,]
        elif self.action == "create" or self.action == "destroy":
            permission_classes = [permissions.IsAuthenticated,IsLowRank]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class GalleryModelViewSet(viewsets.ModelViewSet):
    queryset = GalleryModel.objects.all()
    serializer_class = GalleryModelSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    def get_permissions(self):
        if self.action == "update":
            permission_classes = [permissions.IsAuthenticated,]
        elif self.action == "create" or self.action == "destroy":
            permission_classes = [permissions.IsAuthenticated,IsLowRank]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]