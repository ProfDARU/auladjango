from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    p = Post.objects.all()
    return render(request, 'daru/post_list.html', {'posts':p})