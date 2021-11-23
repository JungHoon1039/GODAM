from django.shortcuts import render, redirect 
from .models import User
from django.core.exceptions import ObjectDoesNotExist
import os, torch
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

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
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    if logged_member :
        return render (req, 'index.html', {'login_member' : logged_member})
    else :
        return render (req,'login.html')

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

# 아이디 중복체크
def check_id(req):
    id = req.GET.get('id')
    try:
        id=User.objects.get(Userid = id)
        duplicate = "fail"
    except:
        duplicate = "pass"
    context = {'duplicate':duplicate}
    return JsonResponse(context)

# 회원정보
def userinfo(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render(req, 'info.html', {'login_member' : logged_member})

# 비밀번호 변경
def password_edit(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render(req, 'edit.html', {'login_member' : logged_member})

# 비밀번호 변경 확인
def password_edit_complete(req):
    try:
        user = User.objects.get(Userid=req.POST.get('id'), Password=req.POST.get('pw'))
        if user:
            user.Password = req.POST.get('new_pw')
            user.save()
            req.session.pop('Userid')
            return render (req,'edit_com.html')
    except ObjectDoesNotExist:
        return redirect (password_edit)

# 회원탈퇴
def member_delete(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render (req, 'delete.html', {'login_member' : logged_member})

# 회원탈퇴 완료
def member_delete_complete(req):
    try:
        del_user = User.objects.get(Userid=req.POST.get('del_id'), Password=req.POST.get('del_pw'))
        if del_user:
            del_user.delete()
            return render(req, 'delete_com.html')
    except ObjectDoesNotExist:
        return redirect (member_delete)

# Create your views here. 
