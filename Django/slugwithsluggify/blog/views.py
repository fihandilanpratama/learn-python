from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
  return HttpResponse('<h1>halaman blog</h1>')

def categoryPost(request, categoryInput):
  posts = Post.objects.filter(category = categoryInput)
  context = {
    'title': 'category post',
    'posts': posts,
    'category': categoryInput,
  }
  return render(request, 'blog/index.html', context)

def singlePost(request, slugInput):
  posts = Post.objects.get(slug=slugInput)

  title = f"<h1>{posts.title}</h1>"
  body = f"<p>{posts.body}</p>"
  category = f"<p>category : {posts.category}</p>"
  slug = f"<p>slug : {posts.slug}</p>"

  return HttpResponse(title + body + category + slug)
  # return HttpResponse("<h1>slug</h1>")