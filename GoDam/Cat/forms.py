from django.forms import ModelForm
from .models import Cat, Board
from User.models import User

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ['Catid','Catimage','Catname','Catage', 'Gender', 'Neutering','Region', 'Discribtion']

class BaseBulletinBoard(ModelForm):
   class Meta:
       model = Board
       fields = '__all__'
