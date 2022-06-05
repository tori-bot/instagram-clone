from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Picture
from .forms import CreatePost
# Create your views here.
def home(request):
    message=f'Hello instagram!'
    pictures=Picture.objects.all()
    context={
        'message':message,
        'pictures':pictures,
    }
    return render(request,'index.html',context)

def upload_pic(request):
    upload=CreatePost()
    if request.method == 'POST':
        upload=CreatePost(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context={
            'upload': upload,
        }
        return render(request,'upload.html',context)

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