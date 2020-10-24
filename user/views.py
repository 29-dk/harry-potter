from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .help_function import getrequest


class GoogleLogin(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self,request):
        data = getrequest(request)
