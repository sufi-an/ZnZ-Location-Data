from django.urls import path, include
from rest_framework.routers import DefaultRouter




from .views import CategoryViewSet, DistrictViewSet, DivisionViewSet, LocationViewSet, ThanaViewSet, UnionViewSet,locationAllPaginationViewset, LocationPictureViewSet, locationAllViewSet, routeViewSet


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
]


## re_path(r'^locationall/$', locationAllViewSet.as_view(),name='locationall'),