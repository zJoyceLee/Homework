from __future__ import unicode_literals

from django.db import models


class Adminuser(models.Model):
    username = models.CharField(primary_key=True, max_length=5)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'AdminUser'

    def __str__(self):
        return username


class Commodity(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=1024)
    price = models.IntegerField()
    store = models.IntegerField()
    info = models.CharField(max_length=10240, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Commodity'


class Image(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    img_path = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'Image'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField()
    total = models.IntegerField()
    status = models.IntegerField()
    username = models.ForeignKey('User', on_delete=models.CASCADE, db_column='username')

    class Meta:
        managed = False
        db_table = 'Orders'


class Ordersinfo(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    counter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'OrdersInfo'
        unique_together = (('order', 'commodity'),)


class Shoppingcart(models.Model):
    username = models.ForeignKey('User', on_delete=models.CASCADE, db_column='username')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    counter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ShoppingCart'
        unique_together = (('username', 'commodity'),)


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=32)
    addr = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'User'

    def __str__(self):
        return username
