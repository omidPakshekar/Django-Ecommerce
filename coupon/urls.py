from django.urls import path, include
from . import views

app_name = 'coupon'
urlpatterns = [
    path('apply/', views.coupon_apply, name='apply'),

]
