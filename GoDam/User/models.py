from django.db import models
 
class User(models.Model):
    Userid = models.CharField(max_length=64, verbose_name='아이디',unique=True)
    Password = models.CharField(max_length=64, verbose_name='비밀번호')
    Nickname = models.CharField(max_length=64, verbose_name='닉네임')
    Username = models.CharField(max_length=64, verbose_name='이름')
    phonenumber = models.CharField(max_length=64, verbose_name='휴대폰번호')
    #city = (('Seoul',"서울시"),('unknown',"미확인"))
    #City = models.CharField(max_length=16, verbose_name='도시', choices=city)
    region = (('강동구','강동구'),('송파구','송파구'),('강남구','강남구'),('서초구','서초구'),('관악구','관악구'),('동작구','동작구'),('금천구','금천구'),('영등포구','영등포구'),('구로구','구로구'),('양천구','양천구'),('강서구','강서구'),('마포구','마포구'),('은평구','은평구'),('서대문구','서대문구'),('종로구','종로구'),('중구','중구'),('용산구','용산구'),('강북구','강북구'),('성북구','성북구'),('동대문구','동대문구'),('성동구','성동구'),('도봉구','도봉구'),('노원구','노원구'),('중랑구','중랑구'),('광진구','광진구'))
    Region = models.CharField(max_length=16, verbose_name='지역',choices=region)
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록')

    #def save(self, * args, ** kwargs):
    #    if self.City == 'Seoul':
    #       self.Region = models.CharField(max_length=16, verbose_name='지역', choices=region)
    #       super(User, self).save( * args, ** kwargs) # Call the "real"
        #save() method.

    # Create your models here.

