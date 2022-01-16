from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
]

handler404 = "mywebsite.views.page_not_found_view"