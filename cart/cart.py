from django.conf import settings
from products.models import Product
from decimal import Decimal
from coupon.models import Coupon

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')



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

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()  )

    def clear(self):
        """
            empty cart
        """
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True


    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id = self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
