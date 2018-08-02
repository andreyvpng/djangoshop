from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{}(Category)'.format(name)


class Product(models.Model):
    name= models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, \
                                 null=True)
    image = models.ImageField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
