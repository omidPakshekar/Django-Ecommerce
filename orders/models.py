from django.conf import settings
from django.db import models
from products.models import Product
from customers.models import CustomUser, Address
from django.utils import timezone
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupon.models import Coupon

class OrderItem(models.Model):
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity        = models.IntegerField(default=1)

    def get_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return "{} * {}".format(self.quantity, self.product.name)


class Order(models.Model):
    user          = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    order_items   = models.ManyToManyField(OrderItem)
    address       = models.ForeignKey(Address, on_delete=models.CASCADE)
    total_price   = models.PositiveIntegerField()
    created_time  = models.DateTimeField(blank=True, null=True, default=timezone.now)
    coupon        = models.ForeignKey(Coupon, on_delete=models.SET_NULL, related_name = 'orders', null = True, blank = True)
    discount      = models.IntegerField(default = 0, validators = [MinValueValidator(0), MaxValueValidator(100)])
    status_type   = [
        ("سفارش ثبت شده","سفارش ثبت شده"),
        ("در حال بسته بندی", "در حال بسته بندی"),
        ("آماده ارسال", "آماده ارسال"),
        ("فرستاده شده", "فرستاده شده"),
        ("دریافت شده است", "دریافت شده است")
    ]
    order_status  = models.CharField(
        max_length=20,
        choices=status_type,
        default="سفارش ثبت شده",
    )

    def __str__(self):
        return self.user.email

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.order_items.all())
        return total_cost - total_cost * ( self.discount / Decimal('100') )
