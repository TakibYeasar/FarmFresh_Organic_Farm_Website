from django.contrib import admin

# Register your models here.

from .models import (
    Articlescategory,
    Articlestag,
    Article,
    ArticleComment,
)

admin.site.register([
    Articlescategory,
    Articlestag,
    Article,
    ArticleComment,
])
