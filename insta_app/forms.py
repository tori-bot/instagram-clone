from django import forms
from .models import Picture,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreatePost(forms.Form):
    title= forms.CharField(max_length=30)
    picture=forms.ImageField()
    caption= forms.CharField(widget=forms.Textarea)
    slug= forms.CharField(max_length=30)

    # class Meta:
    #     model = Picture
    #     exclude = ('author','published','slug','hashtags')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Please input a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password') 

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Please input a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email')  
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields='__all__'
    # profile_picture=forms.ImageField()
    # bio=forms.CharField(widget=forms.Textarea)



# class CommentForm(forms.Form):
#     comment=forms.CharField(max_length=5000)

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)
    

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['comment'].widget.attrs.update({'placeholder':'Add a comment...'})