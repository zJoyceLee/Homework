# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class S(models.Model):
    sno = models.CharField(primary_key=True, max_length=8)
    sname = models.CharField(max_length=255)
    gender = models.CharField(max_length=8)
    age = models.IntegerField()
    sdept = models.CharField(max_length=255)
    pswd = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'S'

    def __str__(self):
        return self.sno


class T(models.Model):
    tno = models.CharField(primary_key=True, max_length=8)
    tname = models.CharField(max_length=255)
    tdept = models.CharField(max_length=255)
    pswd = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'T'

    def __str__(self):
        return self.tno


class C(models.Model):
    cno = models.CharField(primary_key=True, max_length=8)
    cname = models.CharField(max_length=255)
    credit = models.IntegerField()
    cdept = models.CharField(max_length=255)
    tno = models.ForeignKey('T', on_delete=models.CASCADE, db_column='tno')

    class Meta:
        managed = False
        db_table = 'C'


class SC(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    sno = models.ForeignKey(S, on_delete=models.CASCADE, db_column='sno', blank=True, null=True, related_name='sc_sno')
    cno = models.ForeignKey(C, on_delete=models.CASCADE, db_column='cno', blank=True, null=True, related_name='sc_cno')
    grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SC'

    def __str__(self):
        return self.sno


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
