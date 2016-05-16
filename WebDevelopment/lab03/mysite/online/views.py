# from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from online.models import User
from django.views import generic
import json


import hashlib

# Login
def login(request):
    if request.method == 'GET':
        return render(request, 'online/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')

        md5 = hashlib.md5()
        md5.update(passwd.encode())
        passwd_md5 = md5.hexdigest()

        user = User.objects.filter(username = username, passwd = passwd_md5)
        if user:
            response = HttpResponseRedirect('/online/index')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return HttpResponseRedirect('/online/regist/')


# Regist
@csrf_exempt
def regist(request):
    if request.method == 'GET':
        return render(request, 'online/regist.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        birthplace = request.POST.get('birthplace')
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby[]')
        info = request.POST.get('messageArea')

        md5 = hashlib.md5()
        md5.update(password.encode())
        password_md5 = md5.hexdigest()

        User.objects.create(
            username = username,
            passwd = password_md5,
            email = email,
            birthday = birthday,
            birthplace = birthplace,
            gender =  gender,
            hobby = json.dumps(hobby),
            info = info
        )
        return HttpResponse('regist successful.')
        # return HttpResponseRedirect('/online/login/#')


# Login Successful
def index(req):
    username = req.COOKIES.get('username','')
    user = User.objects.get(username = username)
    userdict = {
        'username':username,
        'email': user.email,
        'birthday': user.birthday,
        'birthplace': user.birthplace,
        'gender': user.gender,
        'hobby': user.hobby,
        'info': user.info
    }
    print(userdict)
    return render_to_response(
        'online/index.html',
        userdict
    )

# Logout
def logout(req):
    # response = HttpResponse('Logout !!')
    response = HttpResponseRedirect('/online/login')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def get_user_info(req):
    if req.method == 'GET':
        username = req.COOKIES.get('username','')
        print(username)
        user = User.objects.get(username = username)
        userdict = {
            'username':username,
            'email': user.email,
            'birthday': user.birthday,
            'birthplace': user.birthplace,
            'gender': user.gender,
            'hobby': user.hobby,
            'info': user.info
        }
        print(userdict)
        return JsonResponse(userdict)
