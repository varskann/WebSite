# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# pages/views.py
from django.views.generic import TemplateView, ListView, DetailView
from . models import Post

from django.shortcuts import render, get_object_or_404

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


# def post_detail(request, id):
#     template = 'blog_detail.html'
#     print "Here"
#     blog = get_object_or_404(Post, id=id)
#     context = {
#         'blog': blog,
#     }
#     print blog
#     return render(request, template, context)
#
#
# def post_list(request):
#     template = 'blog.html'
#     objects_list = Post.objects.all()
#     print "Here WTF"
#     context = {
#         'blogs': objects_list,
#     }
#     return render(request, template, context)
