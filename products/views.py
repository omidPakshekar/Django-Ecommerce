from django.shortcuts import render, get_object_or_404
from django.views.generic import ( ListView, DetailView,
                    TemplateView, CreateView, UpdateView,DeleteView)
from .models import Product, ProductImage, Category
from django.urls import reverse_lazy
from cart.forms import CartAddProductForm

class ProductListView(ListView):
    template_name='products/list.html'
    model = Product
    queryset = Product.objects.all()
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Product.objects.get(id=1).product_image.all()[0].image
        return context

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        products = Product.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category_id=category)
        return products

class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    queryset = Product.objects.all()
    context_object_name = 'object'
    # to override The url <int:pk> to <int:id>
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("id")
        image_list = Product.objects.get(id=id_).product_image.all()
        cart_product_form = CartAddProductForm()
        context.update({'image_list': image_list, 'cart_product_form' : cart_product_form})
        return context
    #
    def get_object(self):
        id_ = self.kwargs.get("id")
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, id=id_, slug=slug_)



class ProductDeleteView(DetailView):
    template_name = 'products/delete.html'
    queryset = Product.objects.all()
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self):
        id_ = self.kwargs.get("id")
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, id=id_, slug=slug_)

    def post(self, request, *args, **kwargs):
        print('hi')
        id_ = self.kwargs.get("id")
        slug_ = self.kwargs.get("slug")
        Product.objects.get(id=id_, slug=slug_).delete()
        return render(self.request, 'products/deleted.html', {})
