from django.shortcuts import render, redirect, get_object_or_404
from .forms import CatForm, BaseBulletinBoard
from .models import Cat, Board
import os
from User.models import User

# Create your views here.
#cat create
def catupload(req):
    #post 방식으로 폼을 가져온 경우
    if req.method == "POST":
    #내용물 가져오기
        logged_member = User.objects.get(Userid=req.session.get('Userid'))
        form = CatForm(req.POST,req.FILES)
    #내용물 존재 유무 유효성 검사,확인되면 db저장
        if form.is_valid():
            #form.save(commit=false) 의미는 폼의 내용물을 저장하는데 바로 db에 저장하지 않음,그러니까 완전히 저장하기 전에 사전작업이 있다는 의미
            new_cat = form.save(commit=False)
            #사전작업 = Cat.User 왜래필드를 User 세션에 투입
            new_cat.User = logged_member
            #이제 진짜 저장
            new_cat.save()
            return redirect(catall)
    #아닐 경우 submit 안됨
    else:
        form = CatForm()
    return render(req,'upload.html', {'form': form})

#모든 캣 보이게
def catall(req):
       logged_member = User.objects.filter(Userid=req.session.get('Userid'))
       cat = Cat.objects.all()
       return render(req,'catall.html',{'cat': cat})
#404 에러 기능으로 그 고양이 정보 가져오기
def cat(req,Catid):
       logged_member = User.objects.get(Userid=req.session.get('Userid'))
       cat = get_object_or_404(Cat,pk=Catid)
       return render(req,'catcontent.html',{'i':cat,'owner':logged_member})
#404 에러 기능으로 가져온 고양이 정보 수정
def catedit(req,Catid):
       logged_member = User.objects.get(Userid=req.session.get('Userid'))
       cat = get_object_or_404(Cat,pk=Catid)
       #백앤드 유효성 접근 허용여부
       if logged_member.Userid != cat.User.Userid:
       #이유는 모르겠는데 pathconverter 정의된 def는 리다이렉트 안됨 ㅠㅠ
          return render(req,'catcontent.html',{'i':cat,'owner':logged_member})
       else:
          if req.method == "POST":
          #instance는 저장된걸 의미한다
             form = CatForm(req.POST,req.FILES,instance = cat)
             if form.is_valid():
                form.save()
                return redirect(catall)
          else:
                form = CatForm()
          return render(req,'catedit.html', {'form':form,'cat':cat})

#404 에러 기능으로 가져온 고양이 정보 삭제
def catdelete(req,Catid):
       logged_member = User.objects.get(Userid=req.session.get('Userid'))
       cat = get_object_or_404(Cat,pk=Catid)
       #백앤드 유효성 접근 허용여부
       if logged_member.Userid != cat.User.Userid:
          return render(req,'catcontent.html',{'i':cat,'owner':logged_member})
       else:
          cat.delete()
          return redirect(catall)

# 글 작성
def writePage(req):
    template_name = 'write_page.html'
    if req.method == 'POST':
        form = BaseBulletinBoard(req.POST)
        if form.is_valid():
            form.save()
            return redirect(listPage)
    else:
        form = BaseBulletinBoard()
        context = {
            'form':form,
        }
    return render(req, template_name, context)
    # req.method 가 POST면,
    # form에 req.POST를 이용해 데이터를 집어넣고
    # form을 검증한 뒤, 이게 맞다면 form을 저장해라.
    # 아니면(req.method 가 GET 등)
    # form을 불러오고 context에 넣어서 페이지를 불러오자.

# 글 내용
def showContent(req, id):
    template_name = 'show_content.html'
    board_object = Board.objects.get(id=id)
    context = {
        'board':board_object
    }
    return render(req, template_name, context)

# 글 목록
def listPage(req):
    template_name = 'list_board.html'
    board_object = Board.objects.all()
    context = {
        'boardobject':board_object
    }
    return render(req, template_name, context)

def options(req):
    return render(req, 'options.html')

# 글 수정
def modifyContent(req, id):
    template_name = 'write_page.html'
    instance = get_object_or_404(Board, id=id)
    form = BaseBulletinBoard(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect (listPage)
    context = {
        'form':form
    }
    return render(req, template_name, context)

# 글 삭제
def deleteContent(req, id):
    instance = get_object_or_404(Board, id=id)
    instance.delete()
    return redirect(listPage)




