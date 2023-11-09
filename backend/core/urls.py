from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('banners/', BannerView.as_view()),
    path('featured/', FeaturedView.as_view()),
    path('about/', AboutView.as_view()),
    path('service/', ServiceView.as_view()),
    path('whychoose/', WhychooseView.as_view()),
    path('product/', ProductView.as_view()),
    path('testimonial/', TestimonialView.as_view()),
    path('team/', TeamView.as_view()),
    path('articles-cat/', ArticlescategoryView.as_view()),
    path('articles-tag/', ArticlestagView.as_view()),
    path('articles/', ArticlesView.as_view()),
    path('articles-review/', ArticleReviewView.as_view()),
    path('replay-articles-review/', ReplayArticleReviewView.as_view()),
    path('contact/', ContactView.as_view()),
]