from pyexpat import model
from django.contrib import admin
from .models import Profile,Picture,HashTag,Comment

class PictureAdmin(admin.ModelAdmin):
    model=Picture
    fields=['title','picture','caption','author','published','slug','hashtags','likes']
# Register your models here.

admin.site.register(Profile)
admin.site.register(Picture,PictureAdmin)
admin.site.register(HashTag)
admin.site.register(Comment)
# admin.site.register(Follow)
# admin.site.register(Like)