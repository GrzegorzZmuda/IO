from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework as filters

from OIAPI.logdata.models import Logdata


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Logdata
        fields = ('uptime')