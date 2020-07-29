# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

#登陆页面
@csrf_protect
def index(request):
    return render(request, "login.html", {"err": "", })

#登陆验证
@csrf_protect
def login_view(request):
    username = request.POST['inputEmail']
    password = request.POST['inputPassword']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return render(request, "home.html", )
    else:
        return render(request, "login.html", {"err": '帐号或密码错误!', })

# 登陆后的主页
@csrf_protect
@login_required
def home(request):
    return render(request, "home.html", )

#退出
@csrf_protect
@login_required
def logout_view(request):
    logout(request)
    return render(request, "login.html", {"err": "", })
