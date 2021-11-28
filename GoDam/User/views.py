from django.shortcuts import render, redirect 
from .models import User
from django.core.exceptions import ObjectDoesNotExist
import os, torch
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import re
from django.contrib import messages

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
    new_member = User(Userid=req.POST.get('id'), Password=req.POST.get('pw'), Nickname=req.POST.get('nick'), Username=req.POST.get('name'), phonenumber=req.POST.get('phone'),Region=req.POST.get('region'))
    #소문자 존재하는지 확인(findall는 소문자 끄집어내서 리스트로 만들어버림)
    resulta = re.findall(ps,new_member.Password)
    #얘는 숫자
    resultn = re.findall(pn,new_member.Password)
    #백엔드 아이디 중복검사를 위해 비밀번호 확인 입력 값 가져오기(db저장 X)
    pwd = req.POST.get("pwd")
    #서버 유효성 검사(오류시 폼 전송 안되게) 35번줄 마지막 조건은 입력한 비밀번호와 비밀번호 확인이 되고있는지 서버로 점검
    if new_member.Userid == "" or i.match(new_member.Userid) or len(new_member.Userid) <= 5 or len(new_member.Userid)>=13 or\
       new_member.Password == "" or p.match(new_member.Password) or len(new_member.Password) <= 5 or len(new_member.Password)>=13 or\
       len(resulta) < 1 or len(resultn) < 1 or new_member.Password != pwd or\
       new_member.Nickname == "" or n.match(new_member.Nickname) or len(new_member.Nickname) <= 1 or len(new_member.Nickname) >= 7 or\
       new_member.Username == "" or na.match(new_member.Username) or len(new_member.Username) <= 1 or len(new_member.Username) >= 7 or\
       new_member.phonenumber == "" or new_member.Region == "":
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
     return render(req,'delete_com.html')
#정보 업데이트 변경
def info_edit(req):
    #세션을 가져오는 이유: 각 redirect에서 definition 재실행하라고 요청을 하여 페이지 변환할때 세션을 그대로 남겨지길 위함(render로 html하면 세션이 남아있지 않음)
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render(req, 'info_edit.html', {'login_member' : logged_member})
#정보 업데이트 변경 확인
def info_edit_complete(req):
    logged_member = User.objects.get(Userid=req.session.get('Userid'))
    #새로 입력한 값을 임의 변수로 지정
    nick = req.POST.get('nick')
    phone = req.POST.get('phone')
    region = req.POST.get('region')
    #유효성 검사부터
    if nick == "" or n.match(nick) or len(nick) <= 1 or len(nick) >= 7 or phone == "" or region == "":
        return redirect(info_edit)
    #문제 없으면 새로운 값으로 저장
    else :
        logged_member.Nickname = nick
        logged_member.phonenumber = phone
        logged_member.Region = region
        logged_member.save()
        #필드 세션까지 저장
        req.session['Nickname'] = req.POST.get('nick')
        req.session['phonenumber'] = req.POST.get('phone')
        req.session['Region'] = req.POST.get('region')
        return render(req,"info_edit_com.html")

# 비밀번호 변경
def password_edit(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render(req, 'password_edit.html', {'login_member' : logged_member})

# 비밀번호 변경 확인(info_edit_complete랑 동일)
def password_edit_complete(req):
    logged_member = User.objects.get(Userid=req.session.get('Userid'))
    #현재 비밀번호와 새로운 비밀번호 및 확인 입력받은거 가져와서 변수 지정(셋다 db 저장X )
    pw = req.POST.get('pw')
    new_pw = req.POST.get('new_pw')
    pwd = req.POST.get('pwd')
    #새로 입력 받은 비밀번호 유효성 검사 전제 조건 넣어주기(signup 함수 참고)
    resulta = re.findall(ps,new_pw)
    resultn = re.findall(pn,new_pw)
    # 입력받은 비밀번호와 현재 세션의 비밀번호 같은지 점검
    if logged_member.Password == pw:
    # 같다면 유효성 검사 진행 마지막은 새 비밀번호와 비밀번호가 일치하는지 확인
       if new_pw == "" or p.match(new_pw) or len(new_pw) <= 5 or len(new_pw)>=13 or len(resulta) < 1 or len(resultn) < 1 or new_pw != pwd:
          return redirect (password_edit)
    # 통과되면 새 비번 저장, 세션까지 업데이트
       else:
          logged_member.Password = new_pw
          logged_member.save()
          req.session['Password'] = req.POST.get('pw')
          return render (req,'password_edit_com.html')
    #안되면 리다이렉트(경고 메세지도 비밀번호 변경 페이지에 보내기)
    else:
        messages.warning(req, '기존 비밀번호가 맞는지 확인하세요')
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
