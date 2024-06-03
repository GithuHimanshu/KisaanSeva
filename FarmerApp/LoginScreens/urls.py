from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [

    path('farmerlogin/',farmerlogin),
    path('scholarlogin/',scholarlogin),
    path('add-farmer/',add_farmer),
    path('add-scholar/',add_scholar),
    path('loginfarmer/',loginfarmer),
    path('loginscholar/',loginscholar),
]
