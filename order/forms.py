from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'phone_number', 'city', 'street',
                  'house_number', 'enctance', 'floor', 'apartment',
                  'intercom']
