from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from customers.models import CustomUser

def get_product_image_filepath(self, filename):
    return f'product_images/{self.title + ".png"}'

class ProductImage(models.Model):
    title       = models.CharField(max_length=40)
    image       = models.ImageField(upload_to=get_product_image_filepath,
                                    blank=False, null=False)
    def __str__(self):
        return self.title

class Category(models.Model):
    name            = models.CharField(max_length=40, db_index=True)
    slug            = models.SlugField(max_length=40, db_index=True, unique=True)
    category_parent = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category_id     = models.ForeignKey(Category, related_name='products',
                        on_delete=models.CASCADE, blank=False)
    name            = models.CharField(max_length=40, db_index=True)
    slug            = models.SlugField(max_length=40, db_index=True)
    product_image   = models.ManyToManyField(ProductImage)
    summary         = models.TextField(max_length=100, blank=True, null=True)
    description     = models.TextField(max_length=200, blank=False)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    # discount        =
    stock           = models.PositiveIntegerField(blank=True, null=True)
    rate            = models.PositiveIntegerField(default=0,
                        validators=[MaxValueValidator(5), MinValueValidator(0)])
    available       = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'id': self.id, 'slug':self.slug})


class ProductComment(models.Model):
    product         = models.ForeignKey(Product, related_name='products',
                        on_delete=models.CASCADE, blank=False)
    comment_parent  = models.ForeignKey('ProductComment', null=True, blank=True,
                        on_delete=models.CASCADE)
    user            = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=False, blank=False)
    comment_text    = models.TextField(max_length=100, blank=True, null=True)
    like_count      = models.PositiveIntegerField(default=0, null=True, blank=True)
    dislike_count   = models.PositiveIntegerField(default=0, null=True, blank=True)
