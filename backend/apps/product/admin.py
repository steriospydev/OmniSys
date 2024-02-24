from django.contrib import admin

from .models import Category, SubCategory, Package, Product, Tax

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('product_name', 'package', 'subcategory', 'tax_rate', 'sku_num')

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name', 'category')
    list_editable = ('category',)


admin.site.register(Package)
admin.site.register(Tax)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
