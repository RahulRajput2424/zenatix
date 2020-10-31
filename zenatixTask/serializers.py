from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from zenatixTask.models import User
from django.contrib.auth import authenticate, login

class UserSignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    
    class Meta:
        model = User
        fields = ['email', 'mobileNumber', 'password', 'username']
    
    def create(self, validate_data):
        user = User(mobileNumber=validate_data['mobileNumber'],
        username=validate_data['username'],
        email=validate_data['email'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user