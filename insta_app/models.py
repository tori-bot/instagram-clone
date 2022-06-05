from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class HashTag(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name

class Picture(models.Model):
    name = models.CharField(max_length=50)
    picture=models.ImageField(upload_to='pictures')
    caption=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=100)
    hashtags=models.ManyToManyField(HashTag)

    def __str__(self):
        self.name
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    published=models.DateTimeField(auto_now_add=True)
    picture=models.ForeignKey(Picture, on_delete=models.CASCADE)
    parent_comment=models.ForeignKey('self',on_delete=models.CASCADE)

    def __str__(self):
            self.content
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)   
    profile_picture=models.ImageField(upload_to='profile_pictures',null=True) 
    bio=models.TextField()

    def __str__(self):
        return self.user


