from rest_framework import serializers
from .models import  *
from django.db.models import Count
from rest_framework import permissions, renderers, viewsets, generics, mixins


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class ThanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thana
        fields = '__all__'

class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Union
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class LocationPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationPicture
        fields = '__all__'


class routeSerializer(serializers.ModelSerializer):
    class Meta:
        model = route
        fields = '__all__'

# class locationAllSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = locationAll
#         fields = '__all__'

class UserwithoutPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
    'id',
    'username',
    'phone',
    'auto_enable',
    'time_intervial',
    'vehicle_type',
        ]

class locationAllSerializer(serializers.ModelSerializer):
    division_id = DivisionSerializer(read_only=True)
    district_id = DistrictSerializer(read_only=True)
    thana_id  = ThanaSerializer(read_only=True)
    union_id = UnionSerializer(read_only=True)
    user = UserwithoutPassSerializer(read_only=True)
    category_id = CategorySerializer(read_only=True)
    #url = serializers.HyperlinkedIdentityField(view_name="book-detail", lookup_field='id', read_only=True)
    locationPicture = LocationPictureSerializer( read_only=True)
    class Meta:
        model = Location
        fields = [ 'id', 'lat','long', 'name', 'landmark', 'app_type', 'address', 'user_id','division_id_id', 'locationPicture', 'category_id', 'district_id', 'thana_id','union_id','division_id','created_at','updated_at','user']
        lookup_field = 'id'

        