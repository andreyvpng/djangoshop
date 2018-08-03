from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
]

# Cart
urlpatterns += [
    path('cart/', views.CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), \
         name='cart-add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), \
         name='cart-remove'),
]
