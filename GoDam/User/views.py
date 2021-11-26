from django.shortcuts import render, redirect 
from .models import User
from django.core.exceptions import ObjectDoesNotExist
import os, torch
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import re

#정규식 전역변수 설정해주기
i = re.compile("[^a-zA-Z0-9!~@#$%^&*()_+-=\[\]\{\}<>:`?;'\ \/,.&quot]") #문자 와 숫자특수문자가 아닐때  match()로 받은값 처음부터 다 확인
p = re.compile("[^a-zA-Z0-9]")#문자 와 숫자가 아닐떄 영문/숫자 중 2가지 이상 조합 영문 숫자 최소 1개, 6~12자 이상
n = re.compile("[^0-9a-zA-Z가-힣]")#영어숫자한글이 아닐때 (ex: 중국어 특수문자 사용금지)
na = re.compile("[^가-힣]")#한글이 아닐때
#유효한 저나버노가 아닐떄 그딴거 없음 정신분열 일어남 ㅈㅈ 걍 알아서 치셈
#소문자 모색 초기작업
ps = '[a-z]+'
#얘는 숫자
pn = '[0-9]+'

# 회원가입
def signup(req):
    return render (req, 'signup.html')

# 회원가입 완료 
def signup_com(req):
    new_member = User(Userid=req.POST.get('id'), Password=req.POST.get('pw'), Nickname=req.POST.get('nick'), Username=req.POST.get('name'), phonenumber=req.POST.get('phone'))
    #소문자 존재하는지 확인(findall는 소문자 끄집어내서 리스트로 만들어버림)
    resulta = re.findall(ps,new_member.Password)
    #얘는 숫자
    resultn = re.findall(pn,new_member.Password)
    #서버 유효성 검사(오류시 폼 전송 안되게)
    if new_member.Userid == "" or i.match(new_member.Userid) or len(new_member.Userid) <= 5 or len(new_member.Userid)>=13 or\
       new_member.Password == "" or p.match(new_member.Password) or len(new_member.Password) <= 5 or len(new_member.Password)>=13 or\
       len(resulta) < 1 or len(resultn) < 1 or\
       new_member.Nickname == "" or n.match(new_member.Nickname) or len(new_member.Nickname) <= 1 or len(new_member.Nickname) >= 7 or\
       new_member.Username == "" or na.match(new_member.Username) or len(new_member.Username) <= 1 or len(new_member.Username) >= 7 or\
       new_member.phonenumber == "":
       return render(req,'signup.html')
    else :
       new_member.save()
       return render (req, 'signup_com.html',{'user': new_member})

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

# 로그인
def login(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    if logged_member :
        return render (req, 'index.html', {'login_member' : logged_member})
    else :
        return render (req,'login.html')

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
    return redirect (login)

# 회원정보
def userinfo(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render(req, 'info.html', {'login_member' : logged_member})

# 회원탈퇴 완료
def member_delete_complete(req):
     del_user = User.objects.filter(Userid=req.session.get('Userid'))
     del_user.delete()
     req.session.pop('Userid')
     return render(req, 'delete_com.html')

# 비밀번호 변경
def info_edit(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render(req, 'edit.html', {'login_member' : logged_member})

# 비밀번호 변경 확인
def info_edit_complete(req):
    try:
        user = User.objects.get(Userid=req.POST.get('pw'))
        if user:
            #user.Password = req.POST.get('new_pw')
            logged_member.Password == user
            user.save()
            req.session.pop('Userid')
            req.session['Userid'] = req.POST.get('id')
            return render (req,'edit_com.html')
    except ObjectDoesNotExist:
        return redirect (password_edit)

"""
Id,Pw 정보를 받아 회원탈퇴 - Try문 활용
        try:
            del_user = User.objects.get(Userid=req.POST.get('del_id'), Password=req.POST.get('del_pw'))
            if del_user:
                del_user.delete()
                return render(req, 'delete_com.html')
        except ObjectDoesNotExist:
            return redirect (member_delete)

 Index 페이지 - Login 페이지로 통합됌
 def index(req):
     logged_member = User.objects.filter(Userid=req.session.get('Userid'))
     return render (req, 'index.html', {'login_member' : logged_member})

 회원탈퇴 페이지 - Info 페이지로 통합됌
 def member_delete(req):
     logged_member = User.objects.filter(Userid=req.session.get('Userid'))
     return render (req, 'delete.html', {'login_member' : logged_member})
 """

# Create your views here. 
