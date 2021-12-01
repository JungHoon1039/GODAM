from django.shortcuts import render, redirect
from .forms import CatForm
from .models import Cat
from django.shortcuts import get_object_or_404
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
            return redirect(catuploaded)
    #아닐 경우 submit 안됨
    else:
        form = CatForm()
    return render(req,'upload.html', {'form': form})
#만들어진거 확인
def catuploaded(req):
    logged_member = User.objects.filter(Userid=req.session.get('Userid'))
    return render(req,'uploaded.html')
#모든 캣 보이게
def catall(req):
       logged_member = User.objects.filter(Userid=req.session.get('Userid'))
       cat = Cat.objects.all()
       return render(req,'catall.html',{'cat': cat,'logged_member':logged_member})
#404 에러 기능으로 그 고양이 정보 가져오기
def cat(req,Catid):
       logged_member = User.objects.filter(Userid=req.session.get('Userid'))
       cat = get_object_or_404(Cat,pk=Catid)
       return render(req,'catcontent.html',{'i':cat})


