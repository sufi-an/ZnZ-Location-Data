from django.contrib import admin

from tm_backend.models import *
from import_export import resources
from import_export.admin import ExportActionMixin, ImportExportActionModelAdmin, ExportMixin
#from .models import TruckTypeMaster, Truck, Factory, ProductMaster, Requisition, Trips, Item, req_item


class LocationResource(resources.ModelResource):

    class Meta:
        model = Location
        fields = ('division_id__name', 'district_id__name', 'thana_id__name', 'union_id__name', 'name', 'lat', 'long', 'landmark', 'address', 'user__username', 'created_at')
        export_order = ('division_id__name', 'district_id__name', 'thana_id__name', 'union_id__name', 'name', 'lat', 'long', 'landmark', 'address', 'user__username', 'created_at')


class LocationAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = [LocationResource]
    list_display = ('id', 'division_id', 'district_id', 'thana_id', 'union_id', 'lat', 'long')
    list_filter = ('division_id', 'user', 'category_id', 'created_at')


class RouteResource(resources.ModelResource):
    class Meta:
        model = route
        fields = ('lat', 'long', 'user__username', 'created_at')
        export_order = ('lat', 'long', 'user__username', 'created_at')


class RouteAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = [RouteResource]
    list_display = ('id','lat', 'long', 'user', 'created_at')
    list_filter = ('user', 'created_at')


class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division
        fields = ('id', 'name',)


class DivisionAdmin(ImportExportActionModelAdmin):
    resource_classes = [DivisionResource]
    list_display = ('id', 'name', 'created_at')


class DistrictResource(resources.ModelResource):
    class Meta:
        model = District
        fields = ('id', 'division_id', 'name',)


class DistrictAdmin(ImportExportActionModelAdmin):
    resource_classes = [DistrictResource]
    list_display = ('id', 'division_id', 'name', 'created_at')
    list_filter = ('division_id', )


class ThanaResource(resources.ModelResource):
    class Meta:
        model = Thana
        fields = ('id', 'division_id', 'district_id', 'name',)


class ThanaAdmin(ImportExportActionModelAdmin):
    resource_classes = [ThanaResource]
    list_display = ('id', 'division_id', 'district_id', 'name', 'created_at')
    list_filter = ('division_id', 'district_id')
    search_fields = ['name', 'district_id']


class UnionResource(resources.ModelResource):
    class Meta:
        model = Union
        fields = ('id', 'division_id', 'district_id', 'Thana_id', 'name',)


class UnionAdmin(ImportExportActionModelAdmin):
    resource_classes = [UnionResource]
    list_display = ('id', 'name', 'division_id', 'district_id', 'Thana_id', 'created_at')
    list_filter = ('division_id', 'district_id')
    search_fields = ['name', 'district_id', 'Thana_id']


# from .models import Customer
admin.site.register(Category)
admin.site.register(Division, DivisionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Thana, ThanaAdmin)
admin.site.register(Union, UnionAdmin)
admin.site.register(LocationPicture)
admin.site.register(Location, LocationAdmin)
admin.site.register(route, RouteAdmin)

