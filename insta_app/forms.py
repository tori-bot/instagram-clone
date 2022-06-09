from django import forms
from .models import Picture,Profile


class CreatePost(forms.Form):
    title= forms.CharField(max_length=30)
    picture=forms.ImageField()
    caption= forms.CharField(widget=forms.Textarea)
    

    # class Meta:
    #     model = Picture
    #     exclude = ('author','published','hashtags')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

# class ProfileForm(forms.Form):
#     profile_picture=forms.ImageField()
#     bio=forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    content=forms.CharField(max_length=5000)
    

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['comment'].widget.attrs.update({'placeholder':'Add a comment...'})