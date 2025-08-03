from django import forms
from .models import Room,Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RoomForm(forms.ModelForm):
    
    class Meta:
        model = Room
        fields = ['topic','name','description']


class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields =['body']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'text-black w-full px-3 py-2 border border-white-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500'})
