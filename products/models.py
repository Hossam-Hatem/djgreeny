from email.mime import image
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator , MinValueValidator
from taggit.managers import TaggableManager


# Create your models here.

FLAG_OPTION=(
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale'),
)


class Product(models.Model):
    name = models.CharField(max_length=100 , verbose_name=_('Name'))
    sku = models.IntegerField(_('Sku'))
    subtitle = models.CharField(_("Subtitle") , max_length=500)
    desc = models.TextField(_('description') , max_length=10000)
    price = models.FloatField(_('price'))
    flag = models.CharField(_('Flag') , max_length=10 , choices=FLAG_OPTION)
    quantity = models.IntegerField(_('Quantity'))
    image = models.ImageField(_('Image'),upload_to='product/')
    brand = models.ForeignKey('Brand',related_name='product_brand' ,on_delete=models.SET_NULL,null=True ,blank=True)
    category = models.ForeignKey('Category',related_name='category_brand' ,on_delete=models.SET_NULL,null=True ,blank=True)
    tags = TaggableManager()


    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product , related_name='image_product' ,on_delete=models.CASCADE)
    image = models.ImageField(_('Image'),upload_to='product_image/')

    def __str__(self):
        return str(self.product)

class Brand(models.Model):
    name = models.CharField(_('Name'),max_length=20)
    image = models.ImageField(_('Image'),upload_to='brands/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_('Name'),max_length=20)
    image = models.ImageField(_('Image'),upload_to='category/')

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    rate = models.IntegerField(_('Rate'),validators=(MaxValueValidator(5),MinValueValidator(0)))
    create_at = models.DateTimeField(_('Create at'),default=timezone.now)
    review = models.CharField(_('Review'), max_length=500)

    def __str__(self):
        return str(self.user)


