from django.views import generic

from .models import Product
from .cart import Cart


class ProductListView(generic.ListView):
    model = Product

from django.shortcuts import render


class CartDetailView(generic.View):

    def get(self, request):
        cart = Cart(request)

        return render(request, 'cart/cart_detail.html', {'cart': cart})

from django.shortcuts import get_object_or_404, redirect
from .forms import CartAddProductForm


class CartAddView(generic.View):

    def post(self, request):
        cart = Cart(reques)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cleaned = form.cleaned_data
            cart.add(product=product, quantity=cleaned['quantity'], \
                     cleaned['update'])

        return redirect('cart-detail')


class CartRemoveView(generic.View):

    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)

        return redirect('cart-detail')
