from django.shortcuts import render

# Create your views here.
def home(request):
    message=f'Hello instagram!'
    context={
        'message':message,
    }
    return render(request,'index.html',context)
