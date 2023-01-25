from ctypes import Union
from django.shortcuts import render
from django import views
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, renderers, viewsets, generics
from django_filters import rest_framework as filters

from .models import *
from .serializers import *


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
    # queryset = Location.objects.all().values
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



#-----------
# LocationAll  |
#-----------

# class locationAllViewSet(APIView):
#     queryset=Location.objects.all()
#     serializer_class = locationAllSerializer
#     #permission_classes = [IsAdminUser]
#     @action(detail=True, methods=['get'])
#     def get(self,request):
#         snippet  = Location.objects.all()
#         serializer = self.serializer_class(snippet,many=True)
        
#         return Response(serializer.data,status=status.HTTP_200_OK)
      

    

class locationAllViewSet(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class = locationAllSerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'id']
    # filterset_fields = {'user':['exact'], 'id':['exact']}
    