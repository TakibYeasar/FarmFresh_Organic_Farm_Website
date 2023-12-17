from django.contrib import admin

# Register your models here.

from .models import (
    Articlescategory,
    Articlestag,
    Articles,
    ArticleReview,
    ReplayArticleReview,
)

admin.site.register([
    Articlescategory,
    Articlestag,
    Articles,
    ArticleReview,
    ReplayArticleReview,
])
