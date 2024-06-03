from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home),
    path('aboutus/',aboutus),
    path('blogs/',blogs),
    path('contactus/',contactus),
    path('testimonials/',testimonial),
    path('feedback/',feedback),
    path('scholar/',ScholarUI),
    path('contactusform/',contactusform),
    path('research/',research),
     path('farmerUI/',FarmerUI),
]
