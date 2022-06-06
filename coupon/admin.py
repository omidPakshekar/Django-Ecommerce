from django.contrib import admin
from .models import Coupon
# Register your models here.
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'started_time', 'expired_time', 'discount', 'active']
    list_filter = ['active', 'started_time', 'expired_time']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
