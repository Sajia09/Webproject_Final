from django.db import  models

class PaidCoupon(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    meal = models.CharField(max_length=50)
    date= models.DateField()
