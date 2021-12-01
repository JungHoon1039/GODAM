from django.forms import ModelForm
from .models import Cat#Board
from User.models import User

class CatForm(ModelForm):

    class Meta:
        model = Cat
        fields = ['Catid','Catimage','Catname','Catage','Neutering','Region']

#class BaseBulletinBoard(ModelForm):
#    class Meta:
#        model = Board
#        fields = '__all__'
