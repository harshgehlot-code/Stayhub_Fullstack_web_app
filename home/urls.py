# from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path('hotel-details/<slug>/', views.hotel_details, name="hotel_details")
    # path("login/", views.login_page, name="login_page"),
    # path("register/", views.register, name="register"),
    # path("otp-auth/", views.otp_auth, name="otp_auth")
]