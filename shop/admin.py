from django.contrib import admin
from .models import Category, Product, Region

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','unavailable','created','updated']
    list_editable=['price','stock','unavailable']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)

admin.site.register(Region)
