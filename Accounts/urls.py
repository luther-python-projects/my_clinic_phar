from django.urls import path
from .views import register, sign_in, sign_out, pwd_forget, registration


urlpatterns = [
    path('register', register),
    path('sign_in', sign_in),
    path('sign_out', sign_out),
    path('pwd_forget', pwd_forget),
    path('registration', registration)
    ]
