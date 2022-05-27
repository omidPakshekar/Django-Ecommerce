from django.contrib import admin
from .models import Category, Product, ProductImage, ProductComment
#
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # prepoppulated_fields autmaticly value are set with another field
    prepoppulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category_id', 'price', 'stock', 'available', 'created']
    list_filter = ['available', 'created', 'updated', 'category_id']
    list_editable = ['price', 'stock', 'available']
    prepoppulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductComment)
