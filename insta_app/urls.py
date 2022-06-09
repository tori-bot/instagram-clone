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
    path('profile_form/<int:id>/',views.profile_form,name='profile_form'),
    path('follow/<int:id>/',views.follow, name='follow'),
    path('unfollow/<int:id>/',views.unfollow, name='unfollow'),
    path('add_comment/<int:post_id>/',views.comment, name='add_comment'),
    path('like_post/<int:post_id>/',views.like, name='like_post'),
    path('search/',views.search, name='search'),


]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)