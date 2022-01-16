from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul' : 'about',
    'subjudul' : 'home',
    'banner' : 'about/img/banner-about.jpg',
    'nav' : [
      ['/home', 'home' ],
      ['', ' about-home'],
    ]
  }
  return render(request, 'about/index.html', context)