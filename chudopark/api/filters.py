from django_filters import rest_framework as filters
from .models import *
from .serializers import *

class OrderModelFilter(filters.FilterSet):
    class Meta: 
        model = ProductModel
        fields = ['company']
