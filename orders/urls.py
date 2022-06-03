from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'orders'
urlpatterns = [
    path('checkout/', views.OrderCreateView.as_view(), name='checkout'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail')
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
