from django.forms import ModelForm , TextInput
from .models import city

class city_form(ModelForm):
    class Meta:
        model=city
        fields='__all__'
        widgets={
            'name': TextInput(attrs={ 'class': 'input' , 'placeholder' : 'City Name'}),
        }