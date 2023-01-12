from ctypes import Union
from django.shortcuts import render
from django import views


from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


from .models import Category, District, Division, Location, Thana, Union, LocationPicture, locationAll, route
from .serializers import CategorySerializer, DistrictSerializer, DivisionSerializer, LocationSerializer, ThanaSerializer, UnionSerializer, LocationPictureSerializer, locationAllSerializer, routeSerializer


class Pagination(PageNumberPagination):
    page_size = 10

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()

class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()
    filterset_fields = {'division_id':['exact']}

class ThanaViewSet(viewsets.ModelViewSet):
    serializer_class = ThanaSerializer
    queryset = Thana.objects.all()
    filterset_fields = {'division_id':['exact'], 'district_id':['exact']}

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filterset_fields = {'division_id':['exact'], 'district_id':['exact'],'thana_id':['exact'],'union_id':['exact'],'user':['exact']}

class UnionViewSet(viewsets.ModelViewSet):
    serializer_class = UnionSerializer
    queryset = Union.objects.all()
    filterset_fields = {'division_id':['exact'], 'district_id':['exact'],'Thana_id':['exact']}

class LocationPictureViewSet(viewsets.ModelViewSet):
    serializer_class = LocationPictureSerializer
    queryset = LocationPicture.objects.all()

class routeViewSet(viewsets.ModelViewSet):
    serializer_class = routeSerializer
    queryset = route.objects.all()

class locationAllViewSet(viewsets.ModelViewSet):
    serializer_class = locationAllSerializer
    queryset = locationAll.objects.all()
    filterset_fields = {'user_id':['exact']}