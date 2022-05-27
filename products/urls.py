from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'products'
urlpatterns = [

    path('', views.ProductListView.as_view(), name='list-product'),
    path('<slug:category_slug>/', views.ProductListView.as_view(), name='list-product-category'),
    path('<int:id>/<str:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('delete/<int:id>/<str:slug>/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('update/<int:id>/<str:slug>/', views.ProductDetailView.as_view(), name='product-update')
#
]
