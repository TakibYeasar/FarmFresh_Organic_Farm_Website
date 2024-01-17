from django.contrib import admin

# Register your models here.

from .models import (
    Articlescategory,
    Articlestag,
    ArticleImage,
    Article,
    ArticleComment,
)

admin.site.register([
    Articlescategory,
    Articlestag,
    ArticleImage,
    Article,
    ArticleComment,
])
