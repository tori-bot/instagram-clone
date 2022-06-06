from django.contrib import admin
from .models import Profile,Picture,HashTag,Comment


# Register your models here.

admin.site.register(Profile)
admin.site.register(Picture)
admin.site.register(HashTag)
admin.site.register(Comment)