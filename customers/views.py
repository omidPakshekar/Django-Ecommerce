from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ( ListView, DetailView,
                    TemplateView, CreateView)
from .models import CustomUser
from orders.models import Order

class ProfileView(TemplateView):
    template_name = 'customers/profile.html'

    # redirect = 'orders:order-created'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_ = CustomUser.objects.get(email=self.request.user)
        slug_ = self.kwargs.get('slug')
        order_ = None
        if slug_ == "order-history":
            order_ = Order.objects.filter(user= user_)
            self.template_name = 'customers/order_history.html'
        context.update({'user': user_, 'order_': order_})
        return context
