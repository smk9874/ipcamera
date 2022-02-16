from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<str:mac_addr>/', views.index_mac, name='index_mac'),
#    path('show/<str:mac_addr>/set_alarm/<int:user_id>/', views.set_alarm),
    path('video_feed/', views.video_feed, name='video_feed'),
#    path('recv_mac_addr/<str:mac_addr>/', views.recv_mac_addr, name='recv_mac_addr'),
]
