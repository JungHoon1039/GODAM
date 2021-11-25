from django.db import models
 
class User(models.Model):
    Userid = models.CharField(max_length=64, verbose_name='아이디',unique=True)
    Password = models.CharField(max_length=64, verbose_name='비밀번호')
    Nickname = models.CharField(max_length=64, verbose_name='닉네임')
    Username = models.CharField(max_length=64, verbose_name='이름')
    phonenumber = models.CharField(max_length=64, verbose_name='휴대폰번호')
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록')

# Create your models here.
