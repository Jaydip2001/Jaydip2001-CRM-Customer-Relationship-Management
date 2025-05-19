from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50"/>'
        return "No Image"
    
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'

admin.site.register(Product, ProductAdmin)
from django.contrib import admin

# Register your models here.
