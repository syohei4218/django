from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogModel


class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel
    
class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel
