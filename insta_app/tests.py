from django.test import TestCase
from .models import Picture,Comment,HashTag,Profile
import datetime as dt

# Create your tests here.
class PictureTestClass(TestCase):
    def setUp(self):
        self.picture =Picture(title='image',caption='image description',author=self.user)
        self.picture.save_image()