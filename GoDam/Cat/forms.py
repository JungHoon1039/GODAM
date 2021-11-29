from django.forms import ModelForm
from .models import Cat

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ['Catid','Catimage','Catname','Catage','Neutering','Region']