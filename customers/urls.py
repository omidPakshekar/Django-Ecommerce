from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required, permission_required




app_name = 'customers'
urlpatterns = [
    path('profile/', login_required(views.ProfileView.as_view()), name='profile'),
    path('profile/<slug:slug>/', login_required(views.ProfileView.as_view()), name='customers-slug')
    # path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
