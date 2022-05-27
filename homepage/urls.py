from django.contrib import admin
from django.urls import path, include

from .views import HomePageView


app_name='homepage'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
]
