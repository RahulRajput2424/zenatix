from django.contrib import admin
from django.urls import path
from zenatixTask.views import *

urlpatterns = [
    path('user_signup_view/',UserSignupView.as_view()),
    path('user_login_view/', UserLoginView.as_view()),
    path('add_ingredient/',AddIngredient.as_view()),
    path('add_product/',AddProduct.as_view()),
    path('details_product/', ProductDetails.as_view()),
    path('product_list/', ProductList.as_view()),
    path('place_order/', PlaceOrder.as_view()),
    path('history-order/', OrderDetailsView.as_view()),
]
