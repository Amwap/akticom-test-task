from django.contrib import admin
from .models import *

class TemplateProduct(admin.ModelAdmin):
    search_fields = ('code','name')

admin.site.register(Product, TemplateProduct)
admin.site.register(Level1)
admin.site.register(Level2)
admin.site.register(Level3)
admin.site.register(Unit)

