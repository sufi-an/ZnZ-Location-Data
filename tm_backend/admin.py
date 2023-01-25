from django.contrib import admin

from tm_backend.models import Category, District, Division, Location, LocationPicture, Thana, Union, route

#from .models import TruckTypeMaster, Truck, Factory, ProductMaster, Requisition, Trips, Item, req_item

class UnionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'Thana_id', 'district_id', 'division_id')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'division_id', 'district_id', 'thana_id', 'union_id', 'lat', 'long')


# from .models import Customer
admin.site.register(Category)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Thana)
admin.site.register(Union, UnionAdmin)
admin.site.register(LocationPicture)
admin.site.register(Location, LocationAdmin)
admin.site.register(route)

