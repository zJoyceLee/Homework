from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

@python_2_unicode_compatible
class Form(models.Model):
    form_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.form_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'

@python_2_unicode_compatible
class Field(models.Model):
    form  = models.ForeignKey(Form, on_delete=models.CASCADE)
    field_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    def __str__(self):
        return self.field_text
