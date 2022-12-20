from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('otp/', views.otp, name='otp'),
    path('otpverification/', views.otpVerification, name='otpVerification'),
    path('bookingPage/', views.bookingPage, name='bookingPage'),

]