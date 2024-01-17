from django.contrib import admin

# Register your models here.

from .models import (
    Contactinfo,
    Banner,
    Featured,
    Aboutitem,
    About,
    Serviceitem,
    Service,
    Whychooseitem,
    Whychoose,
    ProductImage,
    Productitem,
    Products,
    Clients,
    Testimonial,
    Team,
    Contact,
)

admin.site.register([
    Contactinfo,
    Banner,
    Featured,
    Aboutitem,
    About,
    Serviceitem,
    Service,
    Whychooseitem,
    Whychoose,
    ProductImage,
    Productitem,
    Products,
    Clients,
    Testimonial,
    Team,
    Contact,
])
