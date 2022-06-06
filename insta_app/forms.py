from django import forms
from .models import Picture


class CreatePost(forms.Form):
    title= forms.CharField(max_length=30)
    picture=forms.ImageField()
    caption= forms.CharField(widget=forms.Textarea)
    slug= forms.CharField(max_length=30)

    # class Meta:
    #     model = Picture
    #     exclude = ('author','published','slug','hashtags')
    
class ProfileForm(forms.Form):
    profile_picture=forms.ImageField()
    bio=forms.CharField(widget=forms.Textarea)

