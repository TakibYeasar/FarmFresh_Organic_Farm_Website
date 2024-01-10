from django.db import models
from authapi.models import CustomUser
from django.shortcuts import reverse
from django.utils.text import slugify
from unidecode import unidecode

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               on_delete=models.CASCADE, verbose_name="Parent Category")
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(
        default="", null=False, allow_unicode=True, db_index=True, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-created',)

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('products:category', args=[self.slug])



class Productitem(models.Model):
    category = models.ManyToManyField(Category, verbose_name="Product Category")
    title = models.CharField(max_length=255, blank=True, null=True)
    photo_main = models.ImageField(
        upload_to='product/', verbose_name="Product Image")
    photo_2 = models.ImageField(upload_to='product/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='product/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='product/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='product/', blank=True, null=True)
    price = models.PositiveBigIntegerField(verbose_name="Product Price")
    old_price = models.PositiveBigIntegerField(
        blank=True, null=True, verbose_name="Product Old Price")
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, allow_unicode=True, db_index=True, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Item'
        ordering = ('-created',)
        
    def get_absolute_url(self):
        return reverse('products:productitem', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'({self.category}) - ({self.title})'


class Products(models.Model):
    background_left = models.ImageField(upload_to='product/', blank=True, null=True)
    background_right = models.ImageField(upload_to='product/', blank=True, null=True)
    item = models.ManyToManyField(Productitem)

    class Meta:
        verbose_name_plural = 'products'

    

class Review(models.Model):
    product = models.ForeignKey(Productitem, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               on_delete=models.CASCADE, verbose_name="Product Review")
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



