# -*-  coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect

from xk.models import S, C, SC
from django.db.models import Avg
from django.core.validators import *
from django.contrib import messages
from django.db import connection

import datetime
import random
import hashlib
import MySQLdb


def student_only(function):
    def wrap(request, *args, **kwargs):
        role = request.session.get('role', None)
        if role and role != 'admin':
            return function(request, *args, **kwargs)
        else:
            return redirect('index')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

# def teacher_only(function):
#     def wrap(request, *args, **kwargs):


def admin_only(function):
    def wrap(request, *args, **kwargs):
        if request.session.get('role', None) == 'admin':
            return function(request, *args, **kwargs)
        else:
            return redirect('index')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def guest_only(function):
    def wrap(request, *args, **kwargs):
        role = request.session.get('role', None)
        if role is None:
            return function(request, *args, **kwargs)
        elif role == 'admin':
            return redirect('tscore')
        else:
            return redirect('scourse')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


# Views definition
@guest_only
def index(request):
    return render(request, 'xk/index.html')


@admin_only
def teacher_manage_score(request, cno=None):
    if cno:
        course = get_object_or_404(C, pk=cno)
    else:
        course = C.objects.all()[0]
    course_list = C.objects.all()
    tmp = [i for i in course_list]
    print(course_list)

    avg_grade = SC.objects.values('cno__cname').annotate(avg_grade=Avg('grade'))
    r = lambda: random.randint(0, 360)
    hue_list = [r() for i in range(0, 10 * len(avg_grade))]
    return render(request, 'xk/teacher_manage_score.html', {
        'course': course,
        'course_list': course_list,
        'avg_grade': avg_grade,
        'hue_list': hue_list,
    })


@admin_only
def teacher_manage_course(request):
    total_course = C.objects.count()
    course_list = C.objects.all()
    return render(request, 'xk/teacher_manage_course.html', {
        'total_course': total_course,
        'course_list': course_list,
    })


@admin_only
def teacher_manage_student(request):
    total_stu = S.objects.count()
    student_list = S.objects.all()
    return render(request, 'xk/teacher_manage_student.html', {
        'total_stu': total_stu,
        'student_list': student_list
    })


@student_only
def student_course(request):
    student = S.objects.get(pk=request.session['role'])
    finished_course_list = [i for i in SC.objects.all() if i.sno.sno == student.sno and i.grade and i.grade >0]
    selected_course_list = [i for i in SC.objects.all() if i.sno.sno == student.sno and not i.grade]
    course_list = C.objects.all()
    return render(request, 'xk/student_course.html', {
        'student': student,
        'finished_course_list': finished_course_list,
        'selected_course_list': selected_course_list,
        'course_list': course_list,
    })


@student_only
def student_score(request):
    student = S.objects.get(pk=request.session['role'])
    finished_course_list = [i for i in SC.objects.all() if i.sno.sno == student.sno and i.grade and i.grade >= 0]
    grade_list = [i.grade for i in finished_course_list]
    if len(grade_list) == 0:
        avg_grade = 0
    else:
        avg_grade = sum(grade_list) / len(grade_list)

    return render(request, 'xk/student_score.html', {
        'student': student,
        'finished_course_list': finished_course_list,
        'avg_grade': avg_grade,
        'date': datetime.datetime.now()
    })


@admin_only
def sc_update(request, sc_id):
    sc = get_object_or_404(SC, pk=sc_id)
    sc.grade = int(request.POST['editScore'])

    try:
        sc.full_clean()
    except ValidationError:
        messages.error(request, u"成绩范围为0~100.")
    else:
        sc.save()
        messages.success(request, u"成绩已修改.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@student_only
def sc_new_or_delete(request):
    if request.POST.get('delete', 'not_delete') == 'value_delete':
        return sc_delete(request)
    elif request.POST.get('delete', 'not_delete') == 'not_delete':
        return sc_new(request)


def sc_new(request):
    student = S.objects.get(pk=request.session['role'])
    selected_course_list = [i.cno.cno for i in SC.objects.all() if i.sno.sno == student.sno and not i.grade]

    try:
        c = C.objects.get(pk=request.POST['cno'])
        ss = "INSERT INTO SC(sno, cno) VALUES ('{}', '{}');".format(student.sno, c.cno)
        print(ss)
        with connection.cursor() as cursor:
            cursor.execute(ss)
        messages.success(request, u"选课成功.")
    except C.DoesNotExist:
        messages.error(request, u"此课程不存在.")
    else:
        if c.cno in selected_course_list:
            messages.error(request, u"已选择此课程.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


def sc_delete(request):
    student = S.objects.get(pk=request.session['role'])

    try:
        course = C.objects.get(pk=request.POST['cno'])
        sc = SC.objects.get(sno_id=student.sno, cno_id=course.cno)
    except C.DoesNotExist:
        messages.error(request, u"此课程不存在.")
    except SC.DoesNotExist:
        messages.error(request, u"未选择此课程.")
    else:
        if sc.grade:
            messages.error(request, u"此课程已有成绩不能退课.")
        else:
            sc.delete()
            messages.success(request, u"退课成功.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def c_new(request):
    new_c = C()
    new_c.cno = (request.POST['inputCno'])
    new_c.cname = (request.POST['inputCname'])
    new_c.credit = int(request.POST['inputCredit'])
    new_c.cdept = (request.POST['inputCdept'])
    new_c.tname = (request.POST['inputTname'])
    cno_list = [c.cno for c in C.objects.all()]

    try:
        new_c.full_clean()
    except ValidationError:
        if new_c.cno in cno_list:
            messages.error(request, u"此课程号已存在.")
        else:
            messages.error(request, u"数据验证失败.")
    else:
        new_c.save()
        messages.success(request, u"添加课程成功.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def c_update(request, c_cno):
    old_c = get_object_or_404(C, pk=c_cno)

    new_c = C()
    new_c.cno = request.POST['inputCno']
    new_c.cname = request.POST['inputCname']
    new_c.credit = int(request.POST['inputCredit'])
    new_c.cdept = request.POST['inputCdept']
    new_c.tname = request.POST['inputTname']

    cno_list_exclude_old_one = [x.cno for x in C.objects.exclude(cno=old_c.cno)]

    try:
        new_c.clean_fields()
    except ValidationError as e:
        messages.error(request, u'数据验证失败.')
    else:
        if new_c.cno == old_c.cno:
            new_c.save()
            messages.success(request, u'修改课程成功.')
        else:
            if new_c.cno in cno_list_exclude_old_one:
                messages.error(request, u"此课程号已存在.")
            else:
                new_c.save()
                old_c_sc_set = old_c.sc_set.all()
                for x in old_c_sc_set:
                    x.cno_id = new_c.cno
                    x.save()
                old_c.delete()
                messages.success(request, u'修改课程成功.')
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def c_delete(request, c_cno):
    c = get_object_or_404(C, pk=c_cno)
    c.delete()
    messages.success(request, u"课程已删除.")
    return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def s_new(request):
    new_s = S()
    new_s.sno = request.POST['inputSno']
    new_s.sname = request.POST['inputSname']
    new_s.sex = request.POST['inputSex']
    new_s.age = request.POST['inputAge']
    new_s.sdept = request.POST['inputSdept']
    new_s.logn = request.POST['inputLogn']
    new_s.pswd = request.POST['inputPswd']
    sno_list = [s.sno for s in S.objects.all()]

    try:
        new_s.full_clean()
    except ValidationError as e:
        if new_s.sno in sno_list:
            messages.error(request, u"此学号已存在.")
        else:
            messages.error(request, u'数据验证错误.')
    else:
        new_s.save()
        messages.success(request, u"添加学生成功.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def s_update(request, s_sno):
    old_s = get_object_or_404(S, pk=s_sno)

    new_s = S()
    new_s.sno = request.POST['inputSno']
    new_s.sname = request.POST['inputSname']
    new_s.sex = request.POST['inputSex']
    new_s.age = request.POST['inputAge']
    new_s.sdept = request.POST['inputSdept']
    new_s.logn = request.POST['inputLogn']
    new_s.pswd = request.POST['inputPswd']

    sno_list_exclude_old_one = [x.sno for x in S.objects.exclude(sno=old_s.sno)]

    try:
        new_s.clean_fields()
    except ValidationError:
        messages.error(request, u"数据验证失败.")
    else:
        if new_s.sno == old_s.sno:
            new_s.save()
            messages.success(request, u'修改学生成功.')
        else:
            if new_s.sno in sno_list_exclude_old_one:
                messages.error(request, u"此学号已存在.")
            else:
                new_s.save()
                old_s_sc_set = old_s.sc_set.all()
                for x in old_s_sc_set:
                    x.sno_id = new_s.sno
                    x.save()
                old_s.delete()
                messages.success(request, u'修改学生成功.')
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def s_delete(request, s_sno):
    s = get_object_or_404(S, pk=s_sno)
    s.delete()
    messages.success(request, u"学生已删除.")
    return redirect(request.META.get('HTTP_REFERER'))


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'admin' and password == 'admin':
        request.session['role'] = 'admin'
        return redirect('tscore')

    try:
        student = S.objects.get(sno=username)
    except S.DoesNotExist:
        messages.error(request, u"帐号或密码错误.")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_md5 = md5.hexdigest()

        if student.pswd == password_md5:
            request.session['role'] = student.sno
            return redirect('sscore')
        else:
            messages.error(request, u"帐号或密码错误.")
            return redirect(request.META.get('HTTP_REFERER'))


def logout(request):
    try:
        del request.session['role']
    except Exception:
        pass
    return redirect('index')
