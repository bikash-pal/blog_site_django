
import django
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
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
    template_name='app_clone/about.html'

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

#############################
@login_required
def publish_post(requset,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

    

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if(request.method=='POST'):
        form=CommentForm(request.POST)
        if(form.is_valid()):
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',post.pk)
    else:
        form=CommentForm()
    return render(request,'app_clone/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
