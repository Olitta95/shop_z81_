from django.contrib import admin
from .models import Category, Promocode, Producer, Discount


admin.site.register(Category)
admin.site.register(Promocode)
admin.site.register(Producer)
admin.site.register(Discount)