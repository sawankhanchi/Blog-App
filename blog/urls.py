from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home, name = 'BlogHome'),
    path('blog/',views.blog, name = 'Blog'),
    path('blogpost/',views.blogpost, name = 'BlogPost'),
    path('contact/',views.contact, name = 'BlogContact'),
    path('about/',views.about, name = 'about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]