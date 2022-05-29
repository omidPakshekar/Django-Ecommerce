from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from customers.models import CustomUser, Address
from django.views.generic import ( ListView, DetailView,
                    TemplateView, CreateView)
from .cart import Cart
from .forms import *

from django.views import View

class OrderCreateView(TemplateView):
    template_name = 'cart/create_order.html'
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
        print(self.request.POST)
        if 'address_id' in self.request.POST:
            print(Address.objects.get(id = int(self.request.POST['address_id'])))
            

        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     # <process form cleaned data>
        #     return HttpResponseRedirect('/success/')

        return redirect('cart:checkout')

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     print("fjfjjjjjj")
    #     form_ = form.save(commit=False)
    #     form_.user = CustomUser.objects.get(email=self.request.user)
    #     form_.save()
    #     return redirect('cart:checkout')

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                update_quantity=cd['update'])
        return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                'quantity' : item['quantity'],
                'update'   : True
        })
    return render(request, 'cart/cart_detail.html', {'cart' : cart})
