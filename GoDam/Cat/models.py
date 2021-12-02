from django.db import models
from User.models import User
import time

# cat image time으로 파일명 등록하는 함수
def _get_upload_to(instance, filename):
    return 'images/%f.jpg' % time.time()

class Cat(models.Model):
      Catid = models.AutoField(primary_key=True)
      Catimage = models.ImageField(upload_to=_get_upload_to, verbose_name='사진')
      Catname = models.CharField(max_length=64, verbose_name='이름')
      Catage = models.IntegerField(verbose_name='나이')
      gender = (("수컷","수컷"),("암컷","암컷"))
      Gender = models.CharField(max_length=16, verbose_name='성별',choices=gender)
      neutering = (("예","예"),("아니오","아니오"))
      Neutering = models.CharField(max_length=16, verbose_name='중성화',choices=neutering)
      #Like = models.IntegerField(verbose_name='좋아요', default = 0)
      region = (('강동구','강동구'),('송파구','송파구'),('강남구','강남구'),('서초구','서초구'),('관악구','관악구'),('동작구','동작구'),('금천구','금천구'),('영등포구','영등포구'),('구로구','구로구'),('양천구','양천구'),('강서구','강서구'),('마포구','마포구'),('은평구','은평구'),('서대문구','서대문구'),('종로구','종로구'),('중구','중구'),('용산구','용산구'),('강북구','강북구'),('성북구','성북구'),('동대문구','동대문구'),('성동구','성동구'),('도봉구','도봉구'),('노원구','노원구'),('중랑구','중랑구'),('광진구','광진구'))
      Region = models.CharField(max_length=16, verbose_name='지역',choices=region)
      Discribtion = models.TextField(verbose_name='설명')
      User = models.ForeignKey("User.User", on_delete=models.CASCADE,db_column="user",verbose_name='등록유저')
      Catupload = models.DateTimeField(auto_now_add=True, verbose_name='등록')


# Create your models here.

class Board(models.Model):
    Catnum = models.ForeignKey("Cat", on_delete=models.CASCADE,db_column="cat", verbose_name='고양이')
    Usernum = models.ForeignKey("User.User", on_delete=models.CASCADE,db_column="user", verbose_name='회원')
    Content = models.TextField(verbose_name='내용')
    Writetime = models.DateTimeField(auto_now_add=True, verbose_name='시간')


