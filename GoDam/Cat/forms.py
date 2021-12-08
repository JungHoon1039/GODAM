from django.forms import ModelForm
from .models import Cat, Board
from User.models import User
from django.core.exceptions import ValidationError
import re

i = re.compile("[!~@#$%^&*()_+-=\[\]\{\}<>:`?;'\ \/,.&quot]")
class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ['Catid','Catimage','Catname','Catage', 'Gender', 'Neutering','Region', 'Discribtion']

    def clean(self):
            cleaned_data = super().clean()
            Catage = cleaned_data.get('Catage')
            Catname = cleaned_data.get('Catname')
            if i.match(Catname):
                raise ValidationError("html 그만 지워, 많이 해먹었잖아")
            if Catage < 0:
                raise ValidationError("html 그만 지워, 많이 해먹었잖아")

class BaseBulletinBoard(ModelForm):
   class Meta:
       model = Board
       fields = ['Content']
