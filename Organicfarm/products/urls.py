from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('products/', GetProductView.as_view(), name='product-list'),
    path('products/<int:id>/', GetProductView.as_view(), name='product-detail'),
    path('products/categories/<str:category>/',
         ProductByCategory.as_view(), name='products-by-category'),
    path('products/<int:product_id>/reviews/create/',
         CreateReviewProduct.as_view(), name='review-create'),
    path('products/<int:product_id>/reviews/',
         GetReviewProducts.as_view(), name='review-list'),
    path('reviews/<int:review_product_id>/update/',
         UpdateReviewProduct.as_view(), name='review-update'),
    path('reviews/<int:review_product_id>/delete/',
         DeleteReviewProduct.as_view(), name='review-delete'),
]
