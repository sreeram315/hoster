from django.conf.urls import url
from django.contrib import admin
from .views import HomeView



urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name = 'manant-home'),
  
]
