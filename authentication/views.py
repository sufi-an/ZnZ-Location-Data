from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User, VehicleType
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
import threading
from rest_framework.response import Response
from .jwtToken import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token, JWTAuthentication
import datetime, random, string
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from .models import User, UserToken, Reset
from .serializers import UserSerializer, vehicleTypeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives


class User_viewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


class LastUserViewSet(APIView):
    def get(self,request):
        queryset = User.objects.last()
        serializer = UserSerializer(queryset)

        return Response(serializer.data)

# class role_master_viewsets(viewsets.ModelViewSet):
#     queryset = role_master.objects.all()
#     serializer_class = role_masterSerializer
#     permission_classes = [IsAuthenticated]

# class UserTypeViewsets(viewsets.ModelViewSet):
#     queryset = UserType.objects.all()
#     serializer_class = UserTypeSerializer
    

# class company_master_viewsets(viewsets.ModelViewSet):
#     queryset = company_master.objects.all()
#     serializer_class = company_masterSerializer
    # permission_classes = [IsAuthenticated]



class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise APIException('Passwords do not match!')

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()


        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        utoken = UserToken.objects.create(
            user_id = user.id,
            token = refresh_token,
            expired_at = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        )


        response = Response()
        # response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)

        response.data = {
            'token': access_token,
            'r_token': refresh_token,

            'email': user.email,
        
            'auto_enable':user.auto_enable,
            'name': user.first_name,
            'id': user.id

        }

        return response


    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        utoken = UserToken.objects.create(
            user_id = user.id,
            token = refresh_token,
            expired_at = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        )
       

        response = Response()
        # response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        
        response.data = {
            'token': access_token,
            'r_token': refresh_token,
            
            'email': user.email,
            'auto_enable':user.auto_enable,
          
            'name': user.first_name,
            'id': user.id
        }
        

        return response


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        refresh_token = request.data['r_token']
        id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter(
            user_id = id,
            token = refresh_token,
            expired_at__gt = datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists:
            raise AuthenticationFailed('unauthenticated')

        access_token = create_access_token(id)
        return Response({
            'token': access_token
        })


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        # refresh_token = request.COOKIES.get('refreshToken')
        refresh_token = request.data['r_token']
        ut = UserToken.objects.filter(token = refresh_token)
        ut.delete()
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }
        return response


class forgotAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        if not validate_email(email):
            return Response({'message': "Enter a valid email address"})

        user = None

        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            return Response({'message': "There is no user registered with the specified E-Mail address."})
        else:
            user = User.objects.filter(email=email).first()

        token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        Reset.objects.create(
            email = email,
            token = token
        )
        
        domain = request.data['path']
        url = domain + '/reset/' + token

        # email_subject='Reset your password!',
        # email_body = render_to_string('authentication/forgetpassword.html', {
        #     'user': user,
        #     'domain': url,
        # })

        # email = EmailMessage(subject=email_subject, body=email_body,
        #                      from_email=settings.EMAIL_FROM_USER,
        #                      to=[email]
        #                      )

        # email.content_subtype = "text/html"

        # if not settings.TESTING:
        #     EmailThread(email).start()

        subject = 'Reset your password!'
        text_content = 'This is an important message.'
        html_content = '<p>Hello,</p><p>Click <a href="%s">here</a> to reset your password!</p><p>Best Regards,</p><p>Techtrioz Team</p>' % url
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_FROM_USER, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()



        return Response({
            'message': "We have sent a password reset link to your email address."
        })



class ResetAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise APIException('Passwords do not match!')


        reset = Reset.objects.filter(token=data['token']).first()

        if not reset:
            raise APIException('Invalid link!')
        
        user = User.objects.filter(email=reset.email).first()

        if not user:
            raise APIException('User not found!')


        user.set_password(data['password'])
        user.save()

        return Response({
            'message': 'success'
        })

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class ResetLinkCheckAPIView(APIView):

    def post(self, request):
        data = request.data
        reset = Reset.objects.filter(token=data['token'],is_visited=False).first()
        if not reset:
            return Response({
                'message': 'Invalid link!'
            })
        else:
            return Response({
                'message': 'success'
            })

class ChangePasswordAPIView(APIView):        

    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            return Response({'message': "Passwords do not match!"})

        userId = ''

        if data['id']:
            userId = data['id']

        user = User.objects.filter(id=userId).first()

        if not user.check_password(request.data['old_password']):
            return Response({'message': "Old Password does not match!"})

        if not user:
            return Response({'message': "Some error occured!"})


        user.set_password(data['password'])
        user.save()

        return Response({'message': 'Password was reset successfully!'})


class vehicleTypeViewSet(viewsets.ModelViewSet):
    serializer_class = vehicleTypeSerializer
    queryset = VehicleType.objects.all()

    

