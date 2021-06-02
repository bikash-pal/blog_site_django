
import django
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DetailView,
                                        CreateView,UpdateView,DeleteView)
#from django.views.generic.edit import DeleteView
#rom django.views.generic.edit import UpdateView
#from django.views.generic.edit import CreateView
#from django.views.generic.detail import DetailView

from .models import Post,Comment
from .forms import Postform,CommentForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

# Create your views here.

class AboutView(TemplateView):
    template_name='about.html'

class PostListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

class PostDetailView(DetailView):
    model=Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'app_clone/post_detail.html'
    form_class=Postform
    model=Post

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'app_clone/post_detail.html'
    form_class=Postform
    model=Post
class DeleatPostView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'app_clone/post_detail.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')