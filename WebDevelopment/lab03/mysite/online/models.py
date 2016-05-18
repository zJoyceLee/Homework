# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    passwd = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    birth_country = models.CharField(max_length=255)
    birth_city = models.CharField(max_length=255)
    gender = models.CharField(max_length=8, blank=True, null=True)
    hobby = models.CharField(max_length=255)
    info = models.CharField(max_length=1024)
    photo_path = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'User'

    def __str__(self):
        return self.username
