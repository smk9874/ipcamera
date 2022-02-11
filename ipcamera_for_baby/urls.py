from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('recv_mac_addr/<str:mac_addr>/', views.recv_mac_addr, name='recv_mac_addr'),
]
