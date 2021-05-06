from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=230, unique=True)
    slug = models.SlugField(max_length=230, unique=True)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_urls(self):
        return reverse('ecommerce_app:products_by_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=230, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=230, unique=True)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_urls(self):
        return reverse('ecommerce_app:prodCat', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
