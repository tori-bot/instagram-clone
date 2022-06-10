from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http.response import Http404
from insta_app.admin import PictureAdmin
from .models import Picture,Profile,Comment,Follow
from django.contrib.auth.models import User
from .forms import CreatePost, ProfileForm,CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    message=f'Hello instagram!'
    pictures=Picture.objects.all().order_by('-published')
    
    context={
        'message':message,
        'pictures':pictures,
    }
    return render(request,'index.html',context)

@login_required(login_url='/accounts/login/')
def onepic(request,pk):
    post = Picture.objects.filter(id=pk).first()
    print(f'\n {post} \n')
    try:
        comments = Comment.objects.filter(picture=post)
        
        print(f'\n {comments} \n')
        
    except Comment.DoesNotExist:  
        comments = None
    
    context = {
        'post':post,
        "comments":comments
        }
    
    return render(request,'onepic.html',context)

@login_required(login_url='/accounts/login/')
def upload_pic(request):
    current_user = request.user
    upload=CreatePost()
    if request.method == 'POST':
        upload=CreatePost(request.POST,request.FILES)
        if upload.is_valid():
            # upload.instance.user=current_user
            # upload.save()
            title = upload.cleaned_data['title']
            picture = upload.cleaned_data['picture']
            caption = upload.cleaned_data['caption']
            pic = Picture(title=title, picture=picture, caption=caption,user=current_user)
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


# @login_required(login_url='/accounts/login/')
def profile_form(request,id):
    current_user = request.user
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    profile_form=ProfileForm()
    if request.method == 'POST':
        profile_form=ProfileForm(request.POST,request.FILES,instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            
            # profile_picture = profile_form.cleaned_data['profile_picture']
            # bio = profile_form.cleaned_data['bio']
            
            # user_profile = Profile(user=current_user, profile_picture=profile_picture, bio=bio)
            # user_profile.save()
            return redirect('profile')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context={
            'profile_form': profile_form, 
        }
        return render(request,'profile_form.html',context)

# @login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    user=User.objects.get(id=current_user.id)
    profile=Profile.get_profile_by_id(user.id)
    follow = Follow.objects.filter(following_id = user.id)
    user_pics=Picture.objects.filter(user=user.id).order_by('-published')
    

    context={
        'user_pics': user_pics,
        'profile':profile,
        'follow':follow,
        'user': user,
    }
    return render(request, 'profile.html', context)

@login_required
def search(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        print(f'\n {search_term} \n')
        searched_profiles = Profile.search_profile(search_term)
        # print(searched_profiles)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"profiles": searched_profiles})
    else:
        message = "Take the chance to search for a profile"

    return render(request, 'search.html', {'message': message})

    
def user_profile(request,username):
    current_user=request.user
    user=User.objects.get(username=current_user.username)
    selected=User.objects.get(username=username)
    if selected==user:
        return redirect('home',username=current_user.username)

    pictures=Picture.objects.filter(user=selected.id)
    follows=Follow.objects.filter(following_id=selected.id)
    profile=Profile.get_profile_by_id(selected.id)
    followers=Follow.objects.filter(followed=selected.id)

    status=False
    for follower in followers:
        if user.id==follower.following.id:
            status=True
            break
        else:
            status=False

    context={
        'user': user,
        'selected': selected,
        'status':status,
        'pictures':pictures,
        'follows':follows,
        'followers':followers,
        'profile':profile,
    }
    return render(request,'user_profile.html',context)

def follow(request,id):
    if request.method == 'GET':
        follow=User.objects.get(pk=id)
        follow_user=Follow(following=request.user, followed=follow)
        follow_user.save()
        return redirect('user_profile' ,username=follow.username)
    
def unfollow(request,id):
    if request.method=='GET':
        unfollow=User.objects.get(pk=id)
        unfollow_user=Follow.objects.filter(following=request.user,followed=unfollow)
        unfollow_user.delete()
        return redirect('user_profile' ,username=unfollow.username)

@login_required(login_url='/accounts/login/')
def comment(request,pic_id):
    current_user = request.user
    if request.method == 'POST':
        comment= request.POST.get('comment')
    post = Picture.objects.get(id=pic_id)
    user_profile = User.objects.get(username=current_user.username)
    new_comment,created=Comment.objects.get_or_create(
         content=comment,
         picture = post,
         user=user_profile   
        )
    new_comment.save()

    return redirect('onepic' ,pk=pic_id)

def like(request,pic_id):
    post = Picture.objects.get(pk=pic_id)
    print(post.id)
    is_liked = False
    user=request.user.profile
    try:
        profile=Profile.objects.get(user=user.user)
        # print(profile)

    except Profile.DoesNotExist:
        raise Http404()
    if post.likes.filter(id=user.user.id).exists():
        post.likes.remove(user.user)
        is_liked=False
    else:
        post.likes.add(user.user)
        is_liked=True
    return HttpResponseRedirect(reverse('home' ))