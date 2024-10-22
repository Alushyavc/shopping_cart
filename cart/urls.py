from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', CartView.as_view(), name='show_cart'),
    path('cart/add/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:pk>/', RemoveItemView.as_view(), name='remove_item_from_cart'),
    path('update-cart-item/<int:pk>/', UpdateCartItemQuantityView.as_view(), name='update_cart_item_quantity'),
]
