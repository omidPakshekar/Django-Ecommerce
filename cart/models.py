from django.conf import settings
from django.db import models
from products.models import Product
from customers.models import CustomUser, Address
from django.utils import timezone

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "{} * {}".format(self.quantity, self.item.title)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    order_items = models.ManyToManyField(OrderItem)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField()
    created_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status_type = [
        ("سفارش ثبت شده","سفارش ثبت شده"),
        ("در حال بسته بندی", "در حال بسته بندی"),
        ("آماده ارسال", "آماده ارسال"),
        ("فرستاده شده", "فرستاده شده"),
        ("دریافت شده است", "دریافت شده است")
    ]
    delivery_status = models.CharField(
        max_length=20,
        choices=status_type,
        default="سفارش ثبت شده",
    )

    def __str__(self):
        return self.user
