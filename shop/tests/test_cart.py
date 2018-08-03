from django.test import TestCase, Client
from django.conf import settings

from ..cart import Cart
from ..models import Category, Product


class CartTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(name="toys")
        Product.objects.create(name='lion', category=category, price=100)
        Product.objects.create(name='cat', category=category, price=150)
        Product.objects.create(name='dog', category=category, price=120)

    def test_add_to_cart(self):
        client = Client()
        cart = Cart(client)
        products = [product for product in Product.objects.all()]

        for product in products:
            cart.add(product)

        # in addition, it checks cart.__iter__
        self.assertEqual([product['product'] for product in cart], products)

    def test_quantity_if_product_in_cart(self):
        client = Client()
        cart = Cart(client)
        product = Product.objects.get(pk=1)

        cart.add(product, quantity=2)
        self.assertEqual(cart.cart['1']['quantity'], 2)

        cart.add(product, quantity=1)
        self.assertEqual(cart.cart['1']['quantity'], 3)

    def test_remove_from_cart(self):
        client = Client()
        cart = Cart(client)
        products = [product for product in Product.objects.all()]

        for product in products:
            cart.add(product)

        cart.remove(Product.objects.get(pk=2))

        self.assertEqual(
            [product['product'] for product in cart],
            [product for product in Product.objects.filter(id__in=[1, 3])]
        )
