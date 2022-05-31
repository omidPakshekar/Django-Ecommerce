from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from customers.models import CustomUser, Address
from django.views.generic import ( ListView, DetailView,
                    TemplateView, CreateView)
from cart.cart import Cart
from .forms import AddressForm
from .models import OrderItem, Order

class OrderCreateView(TemplateView):
    template_name = 'orders/create_order.html'
    model = Product
    address_form = AddressForm
    # redirect = 'orders:order-created'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_ = CustomUser.objects.get(email=self.request.user)
            address_list = Address.objects.filter(user = user_)
            address_form =  AddressForm()
            context.update({'address_list':address_list,'address_form':address_form})
        else:
            print('dumb')
        return context

    def post(self, request, *args, **kwargs):
        if 'address_id' in request.POST:
            address_ = Address.objects.get(id = int(request.POST['address_id']))
            user_ = CustomUser.objects.get(email = request.user)
            cart_ = Cart(request)
            total_price_ = cart_.get_total_price()
            order_items = []
            for i in cart_:
                order_items.append(OrderItem.objects.create(product = i['product'], quantity = i['quantity']))
            order = Order.objects.create(user=user_, address=address_, total_price=total_price_)
            order.order_items.add(*order_items)
            cart_.clear()
            print('afrin')
            # total_price = car
        elif 'create_address' in request.POST:
            form_ = AddressForm(request.POST).save(commit=False)
            form_.user = CustomUser.objects.get(email=request.user)
            form_.save()

        return redirect('orders:checkout')

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     print("fjfjjjjjj")
    #     form_ = form.save(commit=False)
    #     form_.user = CustomUser.objects.get(email=self.request.user)
    #     form_.save()
    #     return redirect('cart:checkout')
