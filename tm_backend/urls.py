from django.urls import path, include
from rest_framework.routers import DefaultRouter




from .views import *


router = DefaultRouter()


router.register('category', CategoryViewSet)
router.register('district', DistrictViewSet)
router.register('thana', ThanaViewSet)
router.register('location', LocationViewSet)
router.register('pic_location', LocationPictureViewSet)
router.register('union', UnionViewSet)
router.register('divison', DivisionViewSet)
router.register('route', routeViewSet)
router.register('locationall', locationAllViewSet)
router.register('location-all-pagination',locationAllPaginationViewset)





urlpatterns = [
    path('', include(router.urls)),
    path('user-location-count/', UserLocationCountViewset.as_view(),
                       name='user-location-count'),
    path('user-route-count/', UserRouteCountViewset.as_view(),
                       name='user-route-count'),
]


## re_path(r'^locationall/$', locationAllViewSet.as_view(),name='locationall'),