from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .help_function import getrequest
from user.models import UserDetails

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.db import transaction


class LoginApi(APIView):

    def post(self,request):
        data = getrequest(request)
        email = data['email']
        password = data['password'] if 'password' in data else None
        is_google_auth = False if password else True

        #Existing User
        user = User.objects.filter(email=email)

        if not user.exists():
            with transaction.atomic():
                user = User.objects.create_user(username=email,email=email)
                if password:
                    user.password = password
                user.save()

                UserDetails.objects.create(user=user,is_google_auth=is_google_auth)

        else:
            if not is_google_auth:
                user = authenticate(username=email,password=password)
                if user is not None:
                    login(request,user)
                else:
                    return Response({'res':0,'msg':'Invalid Credentials!',})
            else:
                user = user.first()

        token, created = Token.objects.get_or_create(user=user)
        if not created:
            if hasattr(user,'auth_token'):
                user.auth_token.delete()
            token , _ = Token.objects.get_or_create(user=user)

        return Response({'res':1,'token':token.key})

