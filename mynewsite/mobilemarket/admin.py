from django.contrib import admin

from .models import Maker, PModel, Product, PPhoto, Store
# Register your models here.

admin.site.register(Maker)
admin.site.register(PModel)
admin.site.register(Product)
admin.site.register(PPhoto)
admin.site.register(Store)

