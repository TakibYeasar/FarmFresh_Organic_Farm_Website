from django.contrib import admin

# Register your models here.

from .models import (
    Cart,
    CartProduct,
    Address,
    Order,
    Payment,
)

admin.site.register([
    Cart,
    CartProduct,
    Address,
    Order,
    Payment,
])
