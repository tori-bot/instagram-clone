from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class HashTag(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name

class Picture(models.Model):
    title = models.CharField(max_length=50)
    picture=models.ImageField(upload_to='pictures')
    caption=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=100)
    hashtags=models.ManyToManyField(HashTag)

    def save_picture(self):
        self.save()

    def delete_picture(self):
        self.delete()

    def update_picture(self,title,picture,caption,author,published,slug,hashtag):
        self.title=title
        self.picture=picture
        self.caption=caption
        self.author=author
        self.published=published
        self.slug=slug
        self.hashtag=hashtag
        self.save()

    @classmethod
    def get_pic_by_id(cls,id):
        picture=cls.objects.get(id=id)
        return picture

    @classmethod
    def search_picture(cls,search_term):
        pictures=cls.objects.filter(hashtags__name__icontains=search_term) 
        return pictures

    def __str__(self):
        self.name
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    published=models.DateTimeField(auto_now_add=True)
    picture=models.ForeignKey(Picture, on_delete=models.CASCADE)
    parent_comment=models.ForeignKey('self',on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
            self.content
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)   
    profile_picture=models.ImageField(upload_to='profile_pictures',null=True) 
    bio=models.TextField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self,user,profile_picture,bio):
        self.user=user
        self.profile_picture=profile_picture
        self.bio=bio
        self.save()

    @classmethod
    def get_profile_by_id(cls,id):
        profile=cls.objects.get(id=id)
        return profile

    @classmethod
    def search_profile(cls,search_term):
        profile=cls.objects.filter(user__name__icontains=search_term) 
        return profile

    def __str__(self):
        return self.user


