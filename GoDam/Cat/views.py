from django.shortcuts import render, redirect
from .forms import CatForm
from .models import Cat

# Create your views here.
def catupload(req):
    #post 방식으로 폼을 가져온 경우
    if req.method == "POST":
    #내용물 가져오기
        form = CatForm(req.POST,req.FILES)
    #내용물 존재 유무 유효성 검사,확인되면 db저장
        if form.is_valid():
            form.save()
            return redirect(catuploaded)
    #아닐 경우 submit 안됨
    else:
        form = CatForm()
    return render(req,'upload.html', {'form': form})
def catuploaded(req):
       return render(req,'uploaded.html')