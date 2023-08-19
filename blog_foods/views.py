from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def index(request):
    """Show all Post."""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def upload(request):
    return render(request, 'upload.html')
def register(request):
    form = UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been regiserted.')
            return redirect('login')
    return render(request,'registration/register.html',{'form':form})