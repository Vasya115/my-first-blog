from django import forms
from .models import Post
from django.contrib.auth.models import User
#from .models import Category
#from .models import Page
from .models import UserProfile
from .models import Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'text',)