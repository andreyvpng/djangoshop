from django.views import generic

from .models import Product
from cart.forms import CartAddProductForm


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()

        return context
