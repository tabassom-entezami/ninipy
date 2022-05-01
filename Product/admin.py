from django.contrib import admin
from .models import *

# each can have own way in admin but I did not had enough time bc uni
# in MaktabFinalProject you can see my codes for this part
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(BaseProduct)
admin.site.register(ProductNumberOne)
admin.site.register(ProductNumberTwo)
admin.site.register(ProductNumberThree)
admin.site.register(SubCategory)
