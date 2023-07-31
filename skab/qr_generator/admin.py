from django.contrib import admin
from .models import Product, Brand, Categorie, Customer, Stock, Sale_item, Sales

# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Categorie)
admin.site.register(Customer)
admin.site.register(Stock)
admin.site.register(Sale_item)
admin.site.register(Sales)