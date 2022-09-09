from django.db import models
from django.utils.translation import gettext as _

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
    brand = ''
    category = ''


    def __str__(self):
        return self.name


class ProductImage(models.Model):
    pass



class Brand(models.Model):
    pass




class Category(models.Model):
    pass



class ProductReview(models.Model):
    pass




