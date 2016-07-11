from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import hashlib

# Login
def login(request):
    if request.method == 'GET':
        return render(request, 'form/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')

        md5 = hashlib.md5()
        md5.update(passwd.encode())
        passwd_md5 = md5.hexdigest()

        user = User.objects.filter(username = username, passwd = passwd_md5)
        if user:
            response = HttpResponseRedirect('/form/index')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return HttpResponseRedirect('/form/regist/')

def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world. You're at the form index.")
    elif request.method == 'POST':
        pass

def info(request):
    if request.method == 'GET':
        return HttpResponse('Information.')

def filling(request):
    if request.method == 'GET':
        return HttpResponse('Filling.')
