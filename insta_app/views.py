from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Picture
from .forms import CreatePost
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    message=f'Hello instagram!'
    pictures=Picture.objects.all()
    context={
        'message':message,
        'pictures':pictures,
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

def profile(request):