from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ['product.name', 'quantity']
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['user', 'created_time', 'total_price', 'address']
#


admin.site.register(OrderItem)
admin.site.register(Order)
