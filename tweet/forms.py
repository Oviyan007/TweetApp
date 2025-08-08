from django import forms
from .models import Tweet,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model =Tweet
        fields =['text','photo']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        