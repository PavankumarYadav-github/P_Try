
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
#    path('login/',login),
   path('register_view/',register_view),
   path('register/',register),
   path('login_view/',login_view),
   path('login/',login),
#    path('dashboard/',coursesData)
]
