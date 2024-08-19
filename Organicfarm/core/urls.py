from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('allproducts/', GetProductView.as_view(), name='all-product-list'),
    path('products/<int:id>/', GetProductView.as_view(), name='product-detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]
