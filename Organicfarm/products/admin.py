from django.contrib import admin

# Register your models here.

from .models import (
    Category,
    Productitem,
    Products,
    Review,
)

admin.site.register([
    Category,
    Productitem,
    Products,
    Review,
])
