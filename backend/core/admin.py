from django.contrib import admin

from .models import (
    Banner,
    Featured,
    Aboutitem,
    About,
    Service,
    Whychooseitem,
    Whychoose,
    Product,
    Testimonial,
    Team,
    Articlescategory,
    Articlestag,
    Articles,
    ArticleReview,
    ReplayArticleReview,
)

admin.site.register([
    Banner,
    Featured,
    Aboutitem,
    About,
    Service,
    Whychooseitem,
    Whychoose,
    Product,
    Testimonial,
    Team,
    Articlescategory,
    Articlestag,
    Articles,
    ArticleReview,
    ReplayArticleReview,
])