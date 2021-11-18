from django.shortcuts import render, redirect 
from .models import User
from django.core.exceptions import ObjectDoesNotExist
import os, torch
from django.views.decorators.csrf import csrf_exempt

# 회원가입
def signup(req):
    return render (req, 'signup.html')

# 회원가입 완료 
def signup_com(req):
    new_member = User(Userid=req.POST.get('id'), Password=req.POST.get('pw'), Nickname=req.POST.get('nick'), Username=req.POST.get('name'), phonenumber=req.POST.get('phone'))
    new_member.save()
    return render (req, 'signup_com.html',{'user': new_member})

# 로그인
def login(req):
    return render (req, 'login.html')

def index(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render (req, 'index.html', {'login_member' : logged_member})

# 로그인 완료&실패
def logged(req):
    logged_member = User.objects.filter(Userid=req.POST.get('id'),Password=req.POST.get('pw'))
    if logged_member :
        req.session['Userid'] = req.POST.get('id')
        return render (req,'index.html', {'login_member' : logged_member})
    else :
        return render (req,'fail.html')

# 세션삭제 - 로그아웃
def logout(req):
    req.session.pop('Userid')
    return render(req, 'logout.html')

# Create your views here. 
