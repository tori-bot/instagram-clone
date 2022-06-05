from django import forms
from .models import Picture

class CreatePost(forms.Form):
    class Meta:
        model=Picture
        fields='__all__'
