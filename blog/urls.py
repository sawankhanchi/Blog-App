from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Blog'
urlpatterns = [
    
    path('',views.home, name = 'BlogHome'),
    path('blog/',views.bloglist, name = 'BlogList'),
    path('blogpost/',views.blogpost, name = 'BlogPost'),
    path('contact/',views.contact, name = 'Contact'),
    path('about/',views.about, name = 'about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]