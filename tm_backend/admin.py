from django.contrib import admin

from tm_backend.models import *
from import_export import resources
from import_export.admin import ExportActionMixin, ImportExportActionModelAdmin, ExportMixin
#from .models import TruckTypeMaster, Truck, Factory, ProductMaster, Requisition, Trips, Item, req_item

class UnionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'Thana_id', 'district_id', 'division_id')


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


# from .models import Customer
admin.site.register(Category)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Thana)
admin.site.register(Union, UnionAdmin)
admin.site.register(LocationPicture)
admin.site.register(Location, LocationAdmin)
admin.site.register(route, RouteAdmin)

