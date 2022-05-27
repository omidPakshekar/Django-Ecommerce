from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product

class HomePageView(TemplateView):
    template_name = "homepage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Product.objects.get(id=1).product_image.all()[0].image
        last_products = Product.objects.all()[:10]
        context.update({'last_products': last_products})
        return context
