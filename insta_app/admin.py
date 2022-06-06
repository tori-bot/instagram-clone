from django.contrib import admin
from .models import Profile,Picture,HashTag,Comment,Follow,Like


# Register your models here.

admin.site.register(Profile)
admin.site.register(Picture)
admin.site.register(HashTag)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Like)