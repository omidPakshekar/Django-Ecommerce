from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .forms import CouponApplyForm
from django.utils import timezone
from .models import Coupon

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        started_time__lte=now,
                                        expired_time__gte=now,
                                        active = True)
            request.session['coupon_id'] = coupon.id
        except :
            request.session['coupon_id'] = None

    return redirect('cart:cart_detail')
