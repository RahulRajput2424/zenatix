import datetime
from rest_framework import  generics
from rest_framework.views import APIView
from rest_framework.response import Response
from zenatixTask.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import  login
from rest_framework import status
from zenatixTask.serializers import UserSignupSerializer

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Successfully Created, Please Sign-In`',
            'data': response.data
        })

