from django.shortcuts import render
from django.views import generic

from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart


class OrderCreateView(generic.View):

    def get(self, request):
        cart = Cart(request)
        form = OrderCreateForm

        return render(request, 'order/order_create.html', \
                      {'cart': cart, 'form': form})

    def post(self, request):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], \
                                price=item['price'], quantity=item['quantity'])

            cart.clear()

        return render(request, 'order/order_create.html', {'order': order})
