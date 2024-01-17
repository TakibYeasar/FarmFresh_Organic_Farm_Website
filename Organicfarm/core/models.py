from django.db import models
from authapi.models import CustomUser
from django.shortcuts import reverse
from django.utils.text import slugify
# Create your models here.

class Contactinfo(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    facebook_link = models.CharField(max_length=255, blank=True, null=True)
    twitter_link = models.CharField(max_length=255, blank=True, null=True)
    linkedin_link = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return self.email


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Banners'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Featured(models.Model):
    image = models.ImageField(upload_to='featured/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Featureds'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Aboutitem(models.Model):
    icon = models.ImageField(upload_to='about/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'About Item'

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    item = models.ManyToManyField(Aboutitem)
    experiance = models.IntegerField(blank=True, null=True)
    specialist = models.IntegerField(blank=True, null=True)
    projects = models.IntegerField(blank=True, null=True)
    clients = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class Serviceitem(models.Model):
    icon = models.ImageField(upload_to='service/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Service Item'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    item = models.ManyToManyField(Serviceitem)

    class Meta:
        verbose_name_plural = 'Service'

    def __str__(self):
        return self.title


class Whychooseitem(models.Model):
    image = models.ImageField(upload_to='whychoose/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Whychoose Item'

    def __str__(self):
        return self.title


class Whychoose(models.Model):
    image = models.ImageField(upload_to='whychoose/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    item = models.ManyToManyField(Whychooseitem)

    class Meta:
        verbose_name_plural = 'Whychoose'

    def __str__(self):
        return str(self.image)
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Images'
        
    def __str__(self):
        return str(self.image)


class Productitem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    main_image = models.ForeignKey(
        ProductImage, related_name='productitem_main_image', on_delete=models.CASCADE, default=1)
    images = models.ManyToManyField(
    ProductImage, related_name='productitem_images', blank=True)
    price = models.PositiveBigIntegerField(verbose_name="Product Price")
    old_price = models.PositiveBigIntegerField(
        blank=True, null=True, verbose_name="Product Old Price")
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(null=False,
                            allow_unicode=True, db_index=True, blank=True, unique=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Item'
        ordering = ('-created',)
    
    def save(self, *args, **kwargs):
        # Use a custom slugify function if desired
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:productitem', args=[self.slug])



class Products(models.Model):
    background_left = models.ImageField(
        upload_to='product/', blank=True, null=True)
    background_right = models.ImageField(
        upload_to='product/', blank=True, null=True)
    item = models.ManyToManyField(Productitem)

    class Meta:
        verbose_name_plural = 'products'


class Clients(models.Model):
    image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(null=False, allow_unicode=True, db_index=True, blank=True, unique=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Clients'
        ordering = ('-created',)
    
    def save(self, *args, **kwargs):
        # Use a custom slugify function if desired
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:clients', args=[self.slug])


class Testimonial(models.Model):
    background = models.ImageField(
        upload_to='testimonial/', blank=True, null=True)
    item = models.ManyToManyField(Clients)

    class Meta:
        verbose_name_plural = 'testimonial'


class Team(models.Model):
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(null=False, allow_unicode=True, db_index=True, blank=True, unique=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Team'
        ordering = ('-created',)
    
    def save(self, *args, **kwargs):
        # Use a custom slugify function if desired
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:team', args=[self.slug])


class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             verbose_name='کاربر', related_name='messages')
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(
        verbose_name='تاریخ ایجاد', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.email
