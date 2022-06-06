from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('upload/',views.upload_pic,name='upload_pic'),
    path('update/<picture_id>',views.pic_update,name='update'),
    path('delete/<picture_id>',views.delete_pic,name='delete'), 
    path('profile/',views.profile,name='profile'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)