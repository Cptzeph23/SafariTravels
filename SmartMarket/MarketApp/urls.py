
from django.contrib import admin
from django.urls import path, include

from MarketApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('destination/', views.destination, name='destination'),
    path('hotel/', views.hotel, name='hotel'),
    path('main/', views.main, name='main'),
]
