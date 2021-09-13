from django.contrib import admin
from .models import User,Cart,Category_products,FeedbackModel,Product,Order,Transactions


# Register your models here.
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Category_products)
admin.site.register(FeedbackModel)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Transactions)
