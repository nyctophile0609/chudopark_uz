from django.contrib import admin
from .models import *
admin.site.register(UserModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(ProductSubsetModel)
admin.site.register(ApplicationModel)
admin.site.register(DiscountModel)
admin.site.register(GalleryModel)