from django.urls import path, include
from .views import (
    SearchBlogListView,
)
app_name = 'Search'
urlpatterns = [
    
    path('',SearchBlogListView.as_view(), name = 'SearchBlog'),
]