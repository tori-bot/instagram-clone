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
        upload=CreatePost(request.POST,request.FILE)
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
