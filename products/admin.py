from django.contrib import admin

# Register your models here.
from .models import Product,Review,CartItem

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(CartItem)
