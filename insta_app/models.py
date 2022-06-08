
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class HashTag(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name

class Picture(models.Model):
    title = models.CharField(max_length=50)
    picture=models.ImageField(upload_to='pictures/')
    caption=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=100,null=True)
    # hashtags=models.ManyToManyField(HashTag)
    

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
    def search_image(cls,search_term):
        images=cls.objects.filter(title__icontains=search_term) 
        return images

    def __str__(self):
        self.name




           
class Profile(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE)   
    profile_picture=models.ImageField(upload_to='profile_pictures/',null=True) 
    bio=models.TextField(default='My Bio', blank=True)
    # followers=models.IntegerField(default=0,null=True)
    @receiver(post_save, sender=User)
    def create_user_profile(self, sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(self,sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self,user,profile_picture,bio):
        self.user=user
        self.profile_picture=profile_picture
        self.bio=bio
        self.save()

    # def get_follows(self):
    #     return self.follow.count()

    # @classmethod
    # def get_profile_by_id(cls,id):
    #     profile=cls.objects.get(id=id)
    #     return profile

    @classmethod
    def search_profile(cls,search_term):
        profile=cls.objects.filter(user__username__icontains=search_term) 
        return profile

    def __str__(self):
        return f'{self.user.username}'

class Comment(models.Model):
    commentor=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True,related_name='commentor')
    comment=models.TextField()
    published=models.DateTimeField(auto_now_add=True)
    picture=models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='comments',null=True)
    # parent_comment=models.ForeignKey('self',on_delete=models.CASCADE,null=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        ordering = ["-published"]


    def __str__(self):
        return f'{self.user.name}'

# class Like(models.Model):
#     image = models.ForeignKey(Picture, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     value= models.IntegerField()
#     date= models.DateTimeField(auto_now_add= True)

#     def __str__(self):
#         return self.user.name

class Follow(models.Model):
    followers = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.followers}'

