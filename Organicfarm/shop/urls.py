from django.urls import path
from .views import *

urlpatterns = [
    path('my-cart/', MyCartView.as_view(), name='my-cart'),
    path('add-to-cart/<int:product_id>/',
         AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/',
         RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('remove-single-item-from-cart/<int:product_id>/',
         RemoveSingleItemFromCartView.as_view(), name='remove-single-item-from-cart'),
    path('delete-cart/', DeleteFullCartView.as_view(), name='delete-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),
]
