from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save #cập nhật user khi đăng ký

class Profile(models.Model):
    # OneToOneField: mỗi user sẽ tương ứng với một profile || khi xóa user account sẽ xóa luôn profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True) #CharFied: người dùng có nhập số điện thoại theo ý muôn(+84 - " "), max_lenght =20: tối đa 20 ký tự, blank = true: cho phép sử dụng khoản cách
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True) # người dùng có thể có nhiều địa chỉ
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

# tự động tạo profile khi đăng ký user 
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance) # khi tạo accout thông tin của user cũng là thông tin profile
            user_profile.save()

# Tự động thêm profile
    post_save.connect(create_profile, sender=User)

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField( max_length=50)
    price = models.DecimalField(default= 0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=50, default= '', blank=True, null= True)
    image = models.ImageField(upload_to= 'uploads/product/')
    # add sale stuff
    is_sale = models.BooleanField(default= False) # nếu false thì không sale và ngược lại
    sale_price  = models.DecimalField(default= 0, decimal_places=2, max_digits=7)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default= '', blank=True)
    phone =  models.CharField(max_length=20, default= '', blank=True)
    date = models.DateField(default= datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
    

    