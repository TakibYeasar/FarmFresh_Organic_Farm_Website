from django.contrib import admin

# Register your models here.

from .models import (
    Category,
    Shippingfaq,
    Additionalinfo,
    Productitem,
    Products,
    Review,
    ReplayReview,
)

admin.site.register([
    Category,
    Shippingfaq,
    Additionalinfo,
    Productitem,
    Products,
    Review,
    ReplayReview,
])
