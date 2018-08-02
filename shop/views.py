from django.views import generic

from .models import Product

class ProductListView(generic.ListView):
    model = Product
