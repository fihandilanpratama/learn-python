from django.shortcuts import render

def index(request):
  context = {
    'judul' : 'home',
    'subjudul': 'home',
    'banner' : 'img/banner-home.jpg',
    'nav' : [
      ['/home', 'Home'],
      ['/blog/home', 'Blog'],
      ['/about/home', 'About'],
    ],
  }
  return render(request, 'index.html', context)

def page_not_found_view(request, exception):
  return render(request, '404.html', status=404)