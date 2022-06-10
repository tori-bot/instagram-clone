from django.test import TestCase
from .models import Picture,Comment,HashTag,Profile
import datetime as dt

# Create your tests here.
class PictureTestClass(TestCase):
    def setUp(self):
        self.picture =Picture(title='image',caption='image description',published='11/2/2022',user=self.user)
        self.picture.save_picture()

        self.comment =Comment(published='11/2/2022',content='image description',user=self.user)

        self.profile =Profile(user='image',bio='image description')
        self.picture.save_picture()

        self.hashtag =HashTag(name='image')
        self.picture.save_picture()

    def tearDown(self):
        Picture.objects.all().delete()
        Profile.objects.all().delete()
        Comment.objects.all().delete()
        HashTag.objects.all().delete()
 
    def test_get_ipicture_id(self):
        picture=Picture.get_picture_by_id()
        self.assertTrue(len(picture)>0)

    def test_search_picture(self):
        term='school'
        results=Picture.search_picture(term)
        self.assertTrue(len(results)==0)