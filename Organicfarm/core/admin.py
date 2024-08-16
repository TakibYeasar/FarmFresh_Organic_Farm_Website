from django.contrib import admin

# Register your models here.

from .models import (
    Contactinfo,
    Banner,
    Featured,
    Service,
    ProductImage,
    Productitem,
    Clients,
    Testimonial,
    Team,
    Contact,
)

admin.site.register([
    Contactinfo,
    Banner,
    Featured,
    Service,
    ProductImage,
    Productitem,
    Clients,
    Testimonial,
    Team,
    Contact,
])
