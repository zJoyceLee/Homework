from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.core.validators import *


class S(models.Model):
    sno = models.CharField(max_length=4, validators=[MaxLengthValidator(4)])
    sno.primary_key = True
    sname = models.CharField(max_length=8, validators=[MaxLengthValidator(8)])
    FEMALE, MALE = 'F', 'M'
    sex_choice = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    sex = models.CharField(max_length=1,
                           choices=sex_choice,
                           default=MALE,
                           validators=[RegexValidator(r'^[MF]$')]
                           )
    age = models.CharField(max_length=2, validators=[MaxLengthValidator(2)])
    sdept = models.CharField(max_length=10, validators=[MaxLengthValidator(10)])
    logn = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    pswd = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])

    def __str__(self):
        return u"{0}-{1}".format(self.sno, self.sname)

    def __unicode__(self):
        return u"{0}-{1}".format(self.sno, self.sname)


class C(models.Model):
    cno = models.CharField(max_length=4, validators=[MaxLengthValidator(4)])
    cno.primary_key = True
    cname = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    credit = models.IntegerField(default=0, validators=[RegexValidator(r'^[46]$')])
    cdept = models.CharField(max_length=20, validators=[MaxLengthValidator(20)])
    tname = models.CharField(max_length=8, validators=[MaxLengthValidator(8)])

    def __str__(self):
        return u"{0}-{1}".format(self.cno, self.cname)

    def __unicode__(self):
        return u"{0}-{1}".format(self.cno, self.cname)


class SC(models.Model):
    sno = models.ForeignKey(S)
    cno = models.ForeignKey(C)
    grade = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        unique_together = ("cno", "sno")

    def __str__(self):  # __unicode__ on Python 2
        return u"{0}-{1}-{2}".format(self.sno, self.cno, self.grade)

    def __unicode__(self):
        return u"{0}-{1}-{2}".format(self.sno, self.cno, self.grade)
