from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',
                                 verbose_name=_('category'))
    name = models.CharField(max_length=200, verbose_name=_('name'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'))
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name=_('image'))
    descriptions = models.TextField(verbose_name=_('descriptions'))
    price = models.IntegerField(verbose_name=_('price'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detail', args=[self.slug, ])
