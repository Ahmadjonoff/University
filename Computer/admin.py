from django.contrib import admin
from .models import Product, Laptop, PC, Printer

admin.site.register(Product)
admin.site.register(Laptop)
admin.site.register(PC)
admin.site.register(Printer)
