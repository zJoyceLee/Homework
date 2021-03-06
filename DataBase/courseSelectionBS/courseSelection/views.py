# -*-  coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from courseSelection.models import Students, Courses, Teachers, Opencourses, Sc
from django.db.models import Avg
from django.core.validators import *
from django.contrib import messages

import datetime
import random

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
    return render(request, 'courseSelection/index.html')


@admin_only
def teacher_manage_score(request, cno=None):
    if cno:
        course = get_object_or_404(Courses, pk=cno)
    else:
        course = Courses.objects.all()[0]
    course_list = Courses.objects.all()
    avg_grade = OpenCourses.objects.values('cno__cname').annotate(avg_grade=Avg('grade'))
    r = lambda: random.randint(0, 360)
    hue_list = [r() for i in range(0, 10 * len(avg_grade))]
    return render(request, 'courseSelection/teacher_manage_score.html', {
        'course': course,
        'course_list': course_list,
        'avg_grade': avg_grade,
        'hue_list': hue_list,
    })


@admin_only
def teacher_manage_course(request):
    total_course = Courses.objects.count()
    course_list = Courses.objects.all()
    return render(request, 'courseSelection/teacher_manage_course.html', {
        'total_course': total_course,
        'course_list': course_list,
    })


@admin_only
def teacher_manage_student(request):
    total_stu = Students.objects.count()
    student_list = Students.objects.all()
    return render(request, 'courseSelection/teacher_manage_student.html', {
        'total_st': total_stu,
        'student_list': student_list
    })


@student_only
def student_course(request):
    student = Students.objects.get(pk=request.session['role'])
#     finished_course_list = [sc for sc in OpenCourses.objects.all() if sc.sno_id == student.sno and sc.grade and sc.grade > 0]
#     selected_course_list = [sc for sc in OpenCourses.objects.all() if sc.sno_id == student.sno]
    course_list = Courses.objects.all()
    return render(request, 'courseSelection/student_course.html', {
        'student': student,
#         'finished_course_list': finished_course_list,
#         'selected_course_list': selected_course_list,
        'course_list': course_list,
    })


@student_only
def student_score(request):
    student = Students.objects.get(pk=request.session['role'])
    for row in Sc.objects.all():
        print(row.grade)
#     finished_course_list = [row for row in Sc.objects.all() if row.student == student.id and row.grade and row.grade > 0]
#     print(finished_course_list)
#     grade_list = [sc.grade for sc in finished_course_list]
#     if len(grade_list) == 0:
#         avg_grade = 0
#     else:
#         avg_grade = sum(grade_list) / len(grade_list)

    return render(request, 'courseSelection/student_score.html', {
        'student': student,
#         'finished_course_list': finished_course_list,
#         'avg_grade': avg_grade,
        'date': datetime.datetime.now()
    })


@admin_only
def sc_update(request, sc_id):
    sc = get_object_or_404(OpenCoursesourses, pk=sc_id)
    sc.grade = int(request.POST['editScore'])

    try:
        sc.full_clean()
    except ValidationError:
        messages.error(request, "成绩范围为0~100.")
    else:
        sc.save()
        messages.success(request, "成绩已修改.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@student_only
def sc_new_or_delete(request):
    if request.POST.get('delete', 'not_delete') == 'value_delete':
        return sc_delete(request)
    elif request.POST.get('delete', 'not_delete') == 'not_delete':
        return sc_new(request)


def sc_new(request):
    student = Students.objects.get(pk=request.session['role'])
    selected_course_list = [sc.cno for sc in OpenCourses.objects.all() if sc.sno_id == student.sno]

    try:
        c = Courses.objects.get(pk=request.POST['cno'])
    except Courses.DoesNotExist:
        messages.error(request, "此课程不存在.")
    else:
        if c in selected_course_list:
            messages.error(request, "已选择此课程.")
        else:
            sc.save()
            messages.success(request, "选课成功.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


def sc_delete(request):
    student = Students.objects.get(pk=request.session['role'])

    try:
        course = Courses.objects.get(pk=request.POST['cno'])
        sc = OpenCourses.objects.get(sno_id=student.sno, cno_id=course.cno)
    except Courses.DoesNotExist:
        messages.error(request, "此课程不存在.")
    except OpenCourses.DoesNotExist:
        messages.error(request, "未选择此课程.")
    else:
        if sc.grade:
            messages.error(request, "此课程已有成绩不能退课.")
        else:
            sc.delete()
            messages.success(request, "退课成功.")
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
    cno_list = [c.cno for c in Courses.objects.all()]

    try:
        new_c.full_clean()
    except ValidationError:
        if new_c.cno in cno_list:
            messages.error(request, "此课程号已存在.")
        else:
            messages.error(request, "数据验证失败.")
    else:
        new_c.save()
        messages.success(request, "添加课程成功.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def c_update(request, c_cno):
    old_c = get_object_or_404(Courses, pk=c_cno)

    new_c = C()
    new_c.cno = request.POST['inputCno']
    new_c.cname = request.POST['inputCname']
    new_c.credit = int(request.POST['inputCredit'])
    new_c.cdept = request.POST['inputCdept']
    new_c.tname = request.POST['inputTname']

    cno_list_exclude_old_one = [x.cno for x in Courses.objects.exclude(cno=old_c.cno)]

    try:
        new_c.clean_fields()
    except ValidationError as e:
        messages.error(request, '数据验证失败.')
    else:
        if new_c.cno == old_c.cno:
            new_c.save()
            messages.success(request, '修改课程成功.')
        else:
            if new_c.cno in cno_list_exclude_old_one:
                messages.error(request, "此课程号已存在.")
            else:
                new_c.save()
                old_c_sc_set = old_c.sc_set.all()
                for x in old_c_sc_set:
                    x.cno_id = new_c.cno
                    x.save()
                old_c.delete()
                messages.success(request, '修改课程成功.')
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def c_delete(request, c_cno):
    c = get_object_or_404(Courses, pk=c_cno)
    c.delete()
    messages.success(request, "课程已删除.")
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
    sno_list = [s.sno for s in Students.objects.all()]

    try:
        new_s.full_clean()
    except ValidationError as e:
        if new_s.sno in sno_list:
            messages.error(request, "此学号已存在.")
        else:
            messages.error(request, '数据验证错误.')
    else:
        new_s.save()
        messages.success(request, "添加学生成功.")
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def s_update(request, s_sno):
    old_s = get_object_or_404(Students, pk=s_sno)

    new_s = S()
    new_s.sno = request.POST['inputSno']
    new_s.sname = request.POST['inputSname']
    new_s.sex = request.POST['inputSex']
    new_s.age = request.POST['inputAge']
    new_s.sdept = request.POST['inputSdept']
    new_s.logn = request.POST['inputLogn']
    new_s.pswd = request.POST['inputPswd']

    sno_list_exclude_old_one = [x.sno for x in Students.objects.exclude(sno=old_s.sno)]

    try:
        new_s.clean_fields()
    except ValidationError:
        messages.error(request, "数据验证失败.")
    else:
        if new_s.sno == old_s.sno:
            new_s.save()
            messages.success(request, '修改学生成功.')
        else:
            if new_s.sno in sno_list_exclude_old_one:
                messages.error(request, "此学号已存在.")
            else:
                new_s.save()
                old_s_sc_set = old_s.sc_set.all()
                for x in old_s_sc_set:
                    x.sno_id = new_s.sno
                    x.save()
                old_s.delete()
                messages.success(request, '修改学生成功.')
    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@admin_only
def s_delete(request, s_sno):
    s = get_object_or_404(Students, pk=s_sno)
    s.delete()
    messages.success(request, "学生已删除.")
    return redirect(request.META.get('HTTP_REFERER'))


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'admin' and password == 'admin':
        request.session['role'] = 'admin'
        return redirect('tscore')

    try:
        student = Students.objects.get(id=username)
    except Students.DoesNotExist:
        messages.error(request, "帐号或密码错误.")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        if student.passwd == password:
            request.session['role'] = student.id
            return redirect('sscore')
        else:
            messages.error(request, "帐号或密码错误.")
            return redirect(request.META.get('HTTP_REFERER'))


def logout(request):
    try:
        del request.session['role']
    except Exception:
        pass
    return redirect('index')
