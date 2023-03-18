from django.db import models
from coupon.models.category import Category


class Coupon(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/coupons/')

    @staticmethod
    def get_all_coupons():
        return Coupon.objects.all()

    @staticmethod
    def get_all_coupons_by_categoryid(category_id):
        if category_id:
            return Coupon.objects.filter(category=category_id)
        else:
            return Coupon.get_all_coupons();

    