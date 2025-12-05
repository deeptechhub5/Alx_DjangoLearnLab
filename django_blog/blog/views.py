from django.shortcuts import render
from .models import Post

def home(request):
    # placeholder homepage
    return render(request, 'blog/base.html')

def posts(request):
    # simple list view (not paginated)
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': posts})
