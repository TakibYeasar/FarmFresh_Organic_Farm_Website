from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('heading-info/', HeadinginfoView.as_view(), name='heading-info'),
    path('banner/', BannerView.as_view(), name='banner'),
    path('featured/', FeaturedView.as_view(), name='featured'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServiceView.as_view(), name='services'),
    path('why-choose-us/', WhychooseView.as_view(), name='why-choose-us'),
    path('products/', ProductsView.as_view(), name='product-list'),
    path('allproducts/', GetProductView.as_view(), name='all-product-list'),
    path('products/<int:id>/', GetProductView.as_view(), name='product-detail'),
    path('testimonials/', TestimonialView.as_view(), name='testimonials'),
    path('team/', TeamView.as_view(), name='team'),
]
