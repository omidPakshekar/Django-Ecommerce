from django.conf import settings
from product.models import Product

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, quantity=1, update_quantity=False):
        """
            add a product to the cart or update it's quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = { 'quantity': 0,
                                    'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update new session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # more the session as 'modified' to sure it's saved
        self.session.modified = True

    def remove(self, product):
        """
            remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
            Iterate over the items in the cart and get the product from database
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the Cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        """
            count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        """
            empty cart
        """
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
    
