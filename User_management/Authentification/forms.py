from django import forms
from .models import User
#DataFlair
class UserCreate(forms.ModelForm):
       class Meta:
            model = User
            fields = '__all__'

  
class ClientCreate(forms.ModelForm):
     class Meta:
          model = User
          fields = ['name' , 'password' , 'email']
       