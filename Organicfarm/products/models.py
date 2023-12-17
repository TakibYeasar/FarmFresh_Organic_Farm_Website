from django.db import models
from authapi.models import CustomUser
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:category", kwargs={
            'slug': self.slug
        })


class Shippingfaq(models.Model):
    question = models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Shipping Faq'
        ordering = ('-created',)

    def __str__(self):
        return self.question


class Additionalinfo(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Additional info'

    def __str__(self):
        return self.title


class Productitem(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255, blank=True, null=True)
    photo_main = models.ImageField(upload_to='product/')
    photo_2 = models.ImageField(upload_to='product/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='product/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='product/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='product/', blank=True, null=True)
    price = models.PositiveBigIntegerField()
    old_price = models.PositiveBigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    additional_info = models.ManyToManyField(Additionalinfo, blank=True)
    faq = models.ManyToManyField(Shippingfaq)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Item'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:productitem", kwargs={
            'slug': self.slug
        })


class Products(models.Model):
    background_one = models.ImageField(upload_to='product/', blank=True, null=True)
    background_two = models.ImageField(upload_to='product/', blank=True, null=True)
    item = models.ManyToManyField(Productitem)

    class Meta:
        verbose_name_plural = 'products'

    


class Review(models.Model):
    product = models.ForeignKey(Productitem, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    comment = models.TextField()
    rate = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'
        ordering = ('-created',)

    def __str__(self):
        return f"To: {self.product} From: {self.customer}"



class ReplayReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    product = models.ForeignKey(Productitem, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    comment = models.TextField()
    rate = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replay Reviews'
        ordering = ('-created',)

    def __str__(self):
        return f"To: {self.review} From: {self.customer}"

