from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='cart-detail'),
    path('add/<int:product_id>/', views.CartAddView.as_view(), \
         name='cart-add'),
    path('remove/<int:product_id>/', views.CartRemoveView.as_view(), \
         name='cart-remove'),
]
