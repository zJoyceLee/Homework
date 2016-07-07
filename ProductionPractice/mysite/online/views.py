# from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from online.models import User
from django.views import generic

import random
import json
import hashlib
from PIL import Image, ImageDraw, ImageFont

# Commodity
def commodity(request):
    if request.method == 'GET':
        return render(request, 'online/commodity.html')

def add_commodity(request):
    if request.method == 'GET':
        return render(request, 'online/add_commodity.html')

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
        captcha = request.POST.get('captcha')
        if captcha != request.session.get('captcha', None):
            return JsonResponse({'code': 1, 'msg': 'invalid captcha'})

        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            email = request.POST.get('email')
            birthday = request.POST.get('birthday')
            birthplace = request.POST.get('birthplace')
            gender = request.POST.get('gender')
            hobby = request.POST.getlist('hobby[]')
            info = request.POST.get('messageArea')
            # photo_path = request.POST.get('photo_path')

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
                info = info,
                # photo_path = photo_path
            )
        except Exception as e:
            return JsonResponse({
                'code': 2,
                'msg': 'Create User failed, error: ' + str(e)
            })
        return JsonResponse({'code': 0, 'msg': 'success'})

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
    return render_to_response(
        'online/index.html',
        userdict
    )

def logout(req):
    response = HttpResponseRedirect('/online/login')
    response.delete_cookie('username')
    return response

def get_user_info(req):
    if req.method == 'GET':
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
        return JsonResponse(userdict)

def gen_captcha(text, response):
    image_width = len(text) * 14
    image_height = 27
    color = (0,0,0,255)
    font = ImageFont.truetype('Ubuntu-B.ttf', 24)

    txt = Image.new('RGB', (image_width, image_height), (255,255,255))
    d = ImageDraw.Draw(txt)
    d.text((0,0), text, font=font, fill=color)
    txt.save(response, "jpeg")

def captcha(req):
    if req.method == 'GET':
        response = HttpResponse(content_type='image/jpeg')
        captcha_str = str(random.randrange(1000, 9999))
        gen_captcha(captcha_str, response)
        req.session['captcha'] = captcha_str
        return response

@csrf_exempt
def update_info(request):
    if request.method == 'POST':
        captcha = request.POST.get('captcha')
        print(captcha)
        if captcha != request.session.get('captcha', None):
            return JsonResponse({'code': 1, 'msg': 'invalid captcha'})
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            email = request.POST.get('email')
            birthday = request.POST.get('birthday')
            birthplace = request.POST.get('birthplace')
            gender = request.POST.get('gender')
            hobby = request.POST.getlist('hobby[]')
            info = request.POST.get('messageArea')
            # photo_path = request.POST.get('photo_path')
            print(info)

            md5 = hashlib.md5()
            md5.update(password.encode())
            password_md5 = md5.hexdigest()

            User.objects.filter(username = username).update(
                passwd = password_md5,
                email = email,
                birthday = birthday,
                birthplace = birthplace,
                gender =  gender,
                hobby = json.dumps(hobby),
                info = info,
                # photo_path = photo_path
            )
        except Exception as e:
            return JsonResponse({
                'code': 2,
                'msg': 'Create User failed, error: ' + str(e)
            })
        return JsonResponse({'code': 0, 'msg': 'success'})
