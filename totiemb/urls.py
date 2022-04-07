from . import views
from django.contrib import admin
from django.urls import path, include
from totiemb.views import get_home, ProductList, get_events, get_about, get_contact


urlpatterns = [
    path('', get_home, name='home'),
    path('product', views.ProductList.as_view(), name='product'),
    path('events', get_events, name='event'),
    path('about', get_about, name='about'),
    path('contact', get_contact, name='contact'),      
] 

