from django.contrib import admin
from .models.coupon import Coupon
from .models.category import Category
from .models.student import Student
from .models.PaidCoupon import PaidCoupon

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Coupon, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Student)
admin.site.register(PaidCoupon)
