from rest_framework import serializers


from .models import  Category, District, Division, Location, Thana, Union, LocationPicture, locationAll, route


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

class locationAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = locationAll
        fields = '__all__'
    