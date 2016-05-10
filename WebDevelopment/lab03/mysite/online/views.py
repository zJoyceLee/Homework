# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from online.models import User
from django.db.models import Avg
from django.core.validators import *
from django.contrib import messages

# Form
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    passwd = forms.CharField(label='密码',widget=forms.PasswordInput())


# Regist
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            passwd = uf.cleaned_data['passwd']
            email = uf.cleaned_data['email']
            question = uf.cleaned_data['question']
            answer = uf.cleaned_data['answer']
            #添加到数据库
            User.objects.create(
                username = username,
                passwd = passwd,
                email = email,
                question = question,
                answer = answer
            )
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

# Login
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            passwd = uf.cleaned_data['passwd']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,passwd__exact = passwd)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/online/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

# Login Successfur
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

# Logout
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response
