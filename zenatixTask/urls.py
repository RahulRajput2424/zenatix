from django.contrib import admin
from django.urls import path
from zenatixTask.views import UserSignupView

urlpatterns = [
    path('user_signup_view/',UserSignupView.as_view()),
    # path('user_login_view/', UserLoginView.as_view()),
]
