from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse

from django.contrib.auth.models import User
from insta_app.admin import PictureAdmin
from .models import Picture,Profile,Comment
from .forms import CreatePost, ProfileForm,CommentForm,SignUpForm, UpdateUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request,id):
    message=f'Hello instagram!'
    pictures=Picture.objects.all().order_by('-published')
    users = User.objects.exclude(id=request.user.id)
    # comments=Comment.objects.filter()

    
    image = get_object_or_404(Comment, pk=id)
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        is_liked = True

    comment_form=CommentForm()
    if request.method == 'POST':
        comment_form=CommentForm(request.POST,request.FILES)
        if comment_form.is_valid():
            savecomment = comment_form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return redirect(reverse('home'))
        else:
            return HttpResponse('Please fill the form correctly.')

    context={
        'message':message,
        'pictures':pictures,
        'users':users,
        'comment_form':comment_form,
        # 'comments':comments,
        'is_liked': is_liked,
        'total_likes': image.total_likes()
    }
    return render(request,'index.html',context)

@login_required(login_url='/accounts/login/')
def upload_pic(request):
    current_user = request.user
    upload=CreatePost()
    if request.method == 'POST':
        upload=CreatePost(request.POST,request.FILES)
        if upload.is_valid():
            # upload.save()
            title = upload.cleaned_data['title']
            picture = upload.cleaned_data['picture']
            caption = upload.cleaned_data['caption']
            slug=upload.cleaned_data['slug']
            pic = Picture(title=title, picture=picture, caption=caption,slug=slug,author=current_user)
            pic.save()
            return redirect('home')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context={
            'upload': upload,
        }
        return render(request,'pic_upload.html',context)

def pic_update(request,picture_id):
    picture_id=int(picture_id)
    try:
        updated=Picture.objects.get(id=picture_id)
    except Picture.DoesNotExist:
        return redirect('home')
    pic_form=CreatePost(request.POST or None,instance=updated)
    if pic_form.is_valid():
        pic_form.save()
        return redirect('home')
    context={
        'pic_form':pic_form,
    }
    return render(request, 'upload.html',context)

def delete_pic(request,picture_id):
    picture_id=int(picture_id)
    try:
        updated=Picture.objects.get(id=picture_id)
    except Picture.DoesNotExist:
        return redirect('home')
    updated.delete()
    return redirect('home')


@login_required(login_url='/accounts/login/')
def profile_form(request):
    current_user = request.user
    profile_form=ProfileForm()
    if request.method == 'POST':
        profile_form=ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            # upload.save()
            
            profile_picture = profile_form.cleaned_data['profile_picture']
            bio = profile_form.cleaned_data['bio']
            
            user_profile = Profile(user=current_user, profile_picture=profile_picture, bio=bio)
            user_profile.save()
            return redirect('profile')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context={
            'profile_form': profile_form, 
        }
        return render(request,'profile_form.html',context)

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile=Profile.objects.filter(id=current_user.id)
    user = User.objects.get(username=current_user.username)
    
    user_pics=Picture.objects.filter(id=current_user.id).order_by('-published')

    context={
        'user_pics': user_pics,
        'user':user,
        'profile':profile,
    }
    return render(request, 'profile.html', context)

def search(request):
    if 'picture' in request.GET and request.GET['picture']:
        #check if the image query exists in our request.GET object and then we then check if it has a value
    
        # search_term=request.GET.get('image')
        # images=Image.search_image(search_term)
        # message=f'(search_term)'
        # return render(request,'search.html',{'images':images,'message':message})

        search_term = request.GET['picture']
        searched_images=Picture.search_image(search_term)
        
        message=f'{search_term} '
        return render(request,'search.html',{'searched_images':searched_images,'message':message})
    else:
        message='Try searching for something'
        return render(request,'search.html',{'message':message})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

