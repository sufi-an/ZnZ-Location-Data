# from django.urls import path
# from . import views

from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views as wpos
from django.contrib.auth import views as auth_views
router = SimpleRouter()

router.register(r"user", wpos.User_viewsets)
#router.register(r'category', wpos.vehicleTypeViewSet)
# router.register(r"role", wpos.role_master_viewsets)
router.register(r"vehicleType", wpos.vehicleTypeViewSet)


# router.register(r"company", wpos.company_master_viewsets)

urlpatterns = [
    path('', include(router.urls)),

    path('last_user',wpos.LastUserViewSet.as_view()),
    path('registers', wpos.RegisterAPIView.as_view()),
    path('logins', wpos.LoginAPIView.as_view()),
    path('currentuser', wpos.UserAPIView.as_view()),
    path('refresh', wpos.RefreshAPIView.as_view()),
    path('logout', wpos.LogoutAPIView.as_view()),

    path('forget', wpos.forgotAPIView.as_view()),
    path('reset', wpos.ResetAPIView.as_view()),
     path('resetlink', wpos.ResetLinkCheckAPIView.as_view()),
     path('changepassword', wpos.ChangePasswordAPIView.as_view())
    
   

     #old

   

    # path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    

]
