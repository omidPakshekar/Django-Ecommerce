from django.db import models
from customers.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Coupon(models.Model):
    class Meta:
        verbose_name_plural = "Coupons"

    user               = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    code               = models.CharField(max_length=50, unique=True)
    started_time       = models.DateTimeField()
    expired_time       = models.DateTimeField()
    discount    = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active      = models.BooleanField(default = True)

    def __str__(self):
        return f"code: {self.code} _precent:  {str(self.discount)}%"
