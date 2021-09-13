from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   U_phone = models.CharField(max_length=20,default=0)
   U_address = models.CharField(max_length=255,default=0)
   
class Cart(models.Model):
    Cart_name = models.TextField(max_length=255)
    Cart_user_id = models.IntegerField(default=0)
    Cart_price = models.IntegerField(default=0)
    Cart_pr_id = models.IntegerField(default=0)
    Cart_quantity = models.IntegerField(default=0)
    Cart_total = models.IntegerField(default=0)
    Cart_coupon = models.IntegerField(default=0)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)


class FeedbackModel(models.Model):
    Fb_title = models.CharField(max_length=255,default=0)   
    Fb_description = models.TextField(default=0)
    Fb_content = models.TextField(default=0)
    Fb_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Fb_user_id = models.IntegerField(default=0)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)

class Category_products(models.Model):
    Cpr_name = models.CharField(max_length=255, default=0)
    Cpr_active = models.BooleanField(default=True)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)

class Product(models.Model):
    Pr_id = models.AutoField(primary_key=True)
    Pr_name = models.CharField(max_length=255)
    Pr_sale = models.BooleanField(default=True)
    Pr_price_sale = models.IntegerField(default=0)
    Pr_price = models.IntegerField(default=0)
    Pr_description = models.TextField(default=0)
    Pr_quantity = models.IntegerField(default=0)
    Pr_category = models.ForeignKey(Category_products, on_delete=models.CASCADE)
    Pr_buy = models.IntegerField(default=0)
    Pr_image = models.CharField(max_length=255,default=0)
    Pr_like = models.IntegerField(default=0)
    Pr_active = models.BooleanField(default=True)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now= False)


class Order(models.Model):
    Od_transaction_id = models.IntegerField(default=0)
    Od_pr_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Od_quantity = models.IntegerField(default=0)
    Od_price = models.IntegerField(default=0)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)


class Transactions(models.Model):
    Tst_email = models.CharField(max_length=50,default=0)
    Tst_name = models.CharField(max_length=50,default=0)
    Tst_address = models.CharField(max_length=50,default=0)
    Tst_phone = models.CharField(max_length=20, default=0)
    Tst_total = models.IntegerField(default=0)
    Tst_status = models.BooleanField(default=True)
    Tst_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Tst_date_buy = models.DateTimeField(default=0) 
    Tst_active = models.BooleanField(default=True)
    
