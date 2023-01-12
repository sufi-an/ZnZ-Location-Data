from django.contrib import admin

from tm_backend.models import Category, District, Division, Location, LocationPicture, Thana, Union, route

#from .models import TruckTypeMaster, Truck, Factory, ProductMaster, Requisition, Trips, Item, req_item


# from .models import Customer
admin.site.register(Category)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Thana)
admin.site.register(Union)
admin.site.register(LocationPicture)
admin.site.register(Location)
admin.site.register(route)

