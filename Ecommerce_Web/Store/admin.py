from django.contrib import admin
from .models import Category,Customer,Product,Order,Profile
from django.contrib.auth.models import User
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)

# Mix profile infor and userinfo
class ProfileInline(admin.StackedInline):
    model = Profile 

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "firsname", "lastname", "email"]
    inlines = [ProfileInline]


# không đăng ký theo cách cũ
admin.site.unregister(User)

# đăng ký theo cách mới

admin.site.register(User, UserAdmin)