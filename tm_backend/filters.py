
from .models import *
from django_filters import rest_framework as filters



class LocationFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Location
        fields = [
            "user",
            "created_at"
        ]


class RouteFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = route
        fields = [
            "user",
            "created_at"
        ]