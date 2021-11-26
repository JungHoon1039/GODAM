from django.db import models
 
class User(models.Model):
    Userid = models.CharField(max_length=64, verbose_name='아이디',unique=True)
    Password = models.CharField(max_length=64, verbose_name='비밀번호')
    Nickname = models.CharField(max_length=64, verbose_name='닉네임')
    Username = models.CharField(max_length=64, verbose_name='이름')
    phonenumber = models.CharField(max_length=64, verbose_name='휴대폰번호')
    #city = (('Seoul',"서울시"),('unknown',"미확인"))
    #City = models.CharField(max_length=16, verbose_name='도시', choices=city)
    region = (('Gangdong-gu','강동구'),('Songpa-gu','송파구'),('Gangnam-gu','강남구'),('Seocho-gu','서초구'),('Gwanak-gu','관악구'),('Dongjak-gu','동작구'),('Geumcheon-gu','금천구'),('Yeongdeungpo-gu','영등포구'),('Guro-gu','구로구'),('Yangcheon-gu','양천구'),('Gangseo-gu','강서구'),('Mapo-gu','마포구'),('Eunpyeong-gu','은평구'),('Seodaemun-gu','서대문구'),('Jongno-gu','종로구'),('Jung-gu','중구'),('Yongsan-gu','용산구'),('Gangbuk-gu','강북구'),('Seongbuk-gu','강북구'),('Dongdaemun-gu','동대문구'),('Seongdong-gu','성동구'),('Dobong-gu','도봉구'),('Nowon-gu','노원구'),('Jungnang-gu','중랑구'),('Gwangjin-gu','광진구'))
    Region = models.CharField(max_length=16, verbose_name='지역',choices=region)
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록')

    #def save(self, * args, ** kwargs):
    #    if self.City == 'Seoul':
    #       self.Region = models.CharField(max_length=16, verbose_name='지역', choices=region)
    #       super(User, self).save( * args, ** kwargs) # Call the "real"
        #save() method.

    # Create your models here.

