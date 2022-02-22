from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<str:mac_addr>/', views.index_mac, name='index_mac'),
    path('show/<str:mac_addr>/<int:user_id>/', views.set_alarm),
    path('motion/alarm/to/server/', views.motion_alarm_to_server),
    path('sound/alarm/to/server/', views.sound_alarm_to_server),
    path('video_feed/', views.video_feed, name='video_feed'),
]
