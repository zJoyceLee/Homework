# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Info(models.Model):
    autokey = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255)
    password = models.ForeignKey('Uploadcode', models.DO_NOTHING, db_column='password')
    name = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=8, blank=True, null=True)
    birthday = models.CharField(max_length=255)
    birthplace = models.CharField(max_length=255)
    info = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Info'


class Uploadcode(models.Model):
    uploadcode = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'Uploadcode'
