from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)

    def __str
