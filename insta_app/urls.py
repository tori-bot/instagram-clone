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
    path('user_profile/<str:username>/',views.user_profile, name='user_profile'),
    path('follow/<int:id>/',views.follow, name='follow'),
    path('unfollow/<int:id>/',views.unfollow, name='unfollow'),
    path('add_comment/<int:pic_id>/',views.comment, name='comment'),
    path('like_post/<int:pic_id>/',views.like, name='like'),
    path('search/',views.search, name='search'),
    path('onepic/<int:pk>/',views.onepic, name='onepic'),


]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)