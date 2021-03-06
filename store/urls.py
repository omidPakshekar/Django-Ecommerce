from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include("orders.urls")),
    path('customers/', include('customers.urls')),
    path('coupons/', include('coupon.urls', namespace='coupon')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
