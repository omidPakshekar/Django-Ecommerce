from django.urls import path, include
from . import views



app_name = 'products'
urlpatterns = [

    path('', views.ProductListView.as_view(), name='list-product'),
    path('<slug:category_slug>/', views.ProductListView.as_view(), name='list-product-category'),
    path('<int:id>/<str:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('delete/<int:id>/<str:slug>/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('update/<int:id>/<str:slug>/', views.ProductDetailView.as_view(), name='product-update')
#
]
