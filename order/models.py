from django.db import models
from django.core.validators import RegexValidator

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.PositiveIntegerField()
    enctance = models.PositiveIntegerField()
    floor = models.PositiveIntegerField()
    apartment = models.PositiveIntegerField()
    intercom = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Oder {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', \
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',
                                on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'OrderItem {}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
