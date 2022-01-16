from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
  posts = Post.objects.all()
  context = {
    'judul' : 'blog',
    'subjudul' : 'home',
    'banner' : 'blog/img/banner-blog.jpg',
    'nav' : [
      ['/home', 'home'],
      ['/blog/home', ' blog-home'],
      ['/blog/cerita', 'blog-cerita'],
      ['/blog/news', 'blog-news'],
    ],
    'posts' : posts,
  }
  return render(request, 'blog/index.html', context)

def cerita(request):
  context = {
    'judul' : 'blog',
    'subjudul' : 'cerita',
    'banner' : 'blog/img/banner-blog.jpg',
    'nav' : [
      ['/home', 'home'],
      ['/blog/home', ' blog-home'],
      ['/blog/cerita', 'blog-cerita'],
      ['/blog/news', 'blog-news'],
    ],
  }
  return render(request, 'blog/index.html', context)



