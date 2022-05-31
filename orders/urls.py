from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'orders'
urlpatterns = [
    path('checkout/', views.OrderCreateView.as_view(), name='checkout'),
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
