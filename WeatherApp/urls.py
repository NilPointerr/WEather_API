from django.contrib import admin
from django.urls import path,include
from .views import Weather_1,index
from WeatherApp.views import index


urlpatterns = [
    path('weather',Weather_1.as_view(),name='weather'),
    path('',index,name="index"),

]
