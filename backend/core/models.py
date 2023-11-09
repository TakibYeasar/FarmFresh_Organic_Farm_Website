from django.db import models
from authapi.models import CustomUser
from django.shortcuts import reverse

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Banners'
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:banner", kwargs={
            'slug': self.slug
        })


class Featured(models.Model):
    image = models.ImageField(upload_to='featured/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Featureds'
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:featured", kwargs={
            'slug': self.slug
        })



class Aboutitem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'About Item'
    
    def __str__(self):
        return self.title



class About(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    item = models.ManyToManyField(Aboutitem, blank=True, null=True)
    experiance = models.CharField(max_length=255, blank=True, null=True)
    specialist = models.CharField(max_length=255, blank=True, null=True)
    projects = models.CharField(max_length=255, blank=True, null=True)
    clients = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'About'
    
    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Service'
    
    def __str__(self):
        return self.title



class Whychooseitem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Whychoose Item'
    
    def __str__(self):
        return self.title



class Whychoose(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    item = models.ManyToManyField(Whychooseitem, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Whychoose'
    
    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Product'
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })


class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Testimonials'
        ordering = ('-created',)
    
    def __str__(self):
        return self.author



class Team(models.Model):
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Team'
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:team", kwargs={
            'slug': self.slug
        })
    

class Articlescategory(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Article Category'
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    
    
class Articlestag(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Article Tags'
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    

class Articles(models.Model):
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    category = models.ManyToManyField(Articlescategory, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Articlestag, blank=True, null=True)
    likes = models.ManyToManyField(CustomUser, null=True, blank=True)
    dislikes = models.ManyToManyField(CustomUser, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Articles'
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:articles", kwargs={
            'slug': self.slug
        })
    
    
class ArticleReview(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    rate = models.IntegerField(default=0, blank=True, null=True)
    likes = models.ManyToManyField(CustomUser, null=True, blank=True)
    dislikes = models.ManyToManyField(CustomUser, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Article Reviews'
        ordering = ('-created',)

    def __str__(self):
        return f"To: {self.product} From: {self.customer}"
    
    
    
class ReplayArticleReview(models.Model):
    review = models.ForeignKey(ArticleReview, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    rate = models.IntegerField(default=0, blank=True, null=True)
    likes = models.ManyToManyField(CustomUser, null=True, blank=True)
    dislikes = models.ManyToManyField(CustomUser, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Replay Article Reviews'
        ordering = ('-created',)

    def __str__(self):
        return f"To: {self.product} From: {self.customer}"




class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Contact'
    
    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse("core:contact", kwargs={
            'slug': self.slug
        })

