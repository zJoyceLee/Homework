# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `# managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Colleges(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        # managed = False
        db_table = 'Colleges'

    def __str__(self):
        return str(self.name)


class Courses(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=255)
    college_name = models.ForeignKey(Colleges, models.CASCADE, db_column='college_name', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Courses'


class Opencourses(models.Model):
    semester = models.CharField(max_length=255)
    course = models.ForeignKey(Courses, models.CASCADE)
    teacher = models.ForeignKey('Teachers', models.CASCADE)
    class_time = models.CharField(max_length=255)
    rated = models.IntegerField(blank=True, null=True)
    num_of_student = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'OpenCourses'
        unique_together = (('semester', 'course', 'teacher', 'class_time'),)


class Sc(models.Model):
    sc_semester = models.ForeignKey(Opencourses, models.CASCADE, related_name='sc_semester')
    SCcourse = models.ForeignKey(Opencourses, models.CASCADE, related_name='sc_courses')
    SCteacher = models.ForeignKey(Opencourses, models.CASCADE, related_name='sc_teacher')
    sc_class_time = models.ForeignKey(Opencourses, models.CASCADE, related_name='sc_class_time')
    student = models.ForeignKey('Students', models.CASCADE)
    grade = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'SC'
        # unique_together = (('sc_semester', 'sc_course', 'sc_teacher', 'sc_class_time', 'student'),)
        unique_together = ['sc_semester', 'SCcourse', 'SCteacher', 'sc_class_time', 'student']


class Students(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=255)
    college_name = models.ForeignKey(Colleges, models.CASCADE, db_column='college_name', blank=True, null=True)
    passwd = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'Students'


class Teachers(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=255)
    college_name = models.ForeignKey(Colleges, models.CASCADE, db_column='college_name')
    passwd = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'Teachers'
