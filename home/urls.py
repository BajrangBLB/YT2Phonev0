from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),

    path('download_video', views.download_video, name="download_video"),
    path('download_audio', views.download_audio, name="download_audio"),

    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('contact_us', views.contact_us, name="contact_us"),

    path('test_mp3', views.test_mp3, name="test_mp3"),
    path('test_360', views.test_360, name="test_360"),
    path('test_720', views.test_720, name="test_720"),
    path('test_480', views.test_480, name="test_480"),

]
