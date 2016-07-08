from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from online.models import User, Adminuser, Commodity
from django.views import generic
from django.contrib import messages

import random
import json
import hashlib
from PIL import Image, ImageDraw, ImageFont

def commodity(request):
    if request.method == 'GET':
        return render(request, 'online/commodity.html')

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
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            addr = request.POST.get('addr')

            md5 = hashlib.md5()
            md5.update(password.encode())
            password_md5 = md5.hexdigest()

            User.objects.create(
                username = username,
                password = password_md5,
                phone = phone,
                email = email,
                addr = addr
            )
        except Exception as e:
            return JsonResponse({
                'code': 2,
                'msg': 'Create User failed, error: ' + str(e)
            })
        return JsonResponse({'code': 0, 'msg': 'success'})


# Login
def login(request):
    if request.method == 'GET':
        return render(request, 'online/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        md5 = hashlib.md5()
        md5.update(password.encode())
        passwd_md5 = md5.hexdigest()

        user = Adminuser.objects.filter(username = username, password = passwd_md5)
        if user:
            response = HttpResponseRedirect('/online/add_commodity/')
            response.set_cookie('username', username, 3600)
            return HttpResponseRedirect('/online/add_commodity/')
        else:
            return HttpResponseRedirect('/online/')

@csrf_exempt
def add_commodity(request):
    if request.method == 'GET':
        return render(request, 'online/add_commodity.html')
    elif request.method == 'POST':
        try:
                id = request.POST.get('id')
                name = request.POST.get('name')
                price = request.POST.get('price')
                store = request.POST.get('store')
                info = request.POST.get('messageArea')

                Commodity.objects.create(
                    id = id,
                    name  = name,
                    price  = price,
                    store = store,
                    info = info
                )
        except Exception as e:
            return JsonResponse({
                'code': 2,
                'msg': 'Create Commodity failed, error: ' + str(e)
            })
        return JsonResponse({'code': 0, 'msg': 'success'})

def logout(req):
    response = HttpResponseRedirect('/online/')
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
