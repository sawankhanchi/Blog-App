from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView,TemplateView

class SearchBlogListView(TemplateView):
    template_name = 'search/view.html'

    
