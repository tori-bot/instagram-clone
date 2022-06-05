from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('upload/',views.upload_pic,name='upload_pic'),
    path('update/<picture_id>',views.pic_update,name='update'),
    path('delete/<picture_id>',views.delete_pic,name='delete'), 
]