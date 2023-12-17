from django.db import models
from authapi.models import CustomUser
from products.models import Productitem

# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    complete = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)


class CartProduct(models.Model):
    product = models.ForeignKey(Productitem,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Cart=={self.cart.id}<==>CartProduct:{self.id}==Qualtity=={self.quantity}"


class Address(models.Model):
    user = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    is_default = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} => {self.email}"


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, blank=True)
    billing_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, blank=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    discount = models.DecimalField(decimal_places=2, max_digits=8)
    total = models.DecimalField(decimal_places=2, max_digits=8)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    payment_complete = models.BooleanField(
        default=False, blank=True, null=True)
    date = models.DateField(auto_now_add=True)


PAYMENT_METHOD = (
    ('paypal', 'PayPal'),
    ('stripe', 'stripe'),
)

class Payment(models.Model):
    buyer = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return self.stripe_charge_id
