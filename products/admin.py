from django.contrib import admin
from .models import Product , Brand , Category , ProductImage , ProductReview
# Register your models here.

class ProductImageTabular(admin.TabularInline):
    model=ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name', 'flag','euantity','price']
    list_filter = ['flag','brand','category']
    search_fields = ['name','desc','subtitle']

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductReview)

