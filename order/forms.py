from django import forms

from .models import Order


class OrderCreateForm(models.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'phone_number', 'city', 'street', \
                  'house_number', 'entrance', 'floor', 'apartment', \
                  'intercom']
