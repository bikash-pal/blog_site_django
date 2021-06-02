from django.db import models
from django.db.models.base import Model
from django.utils import timezone 
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.CharField(max_length=1000)
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(default=False,null=True)

    def publish(self):
        Post.published_date=timezone.now()
        Post.save()
        
        #given in turorial like this
        '''self.published_date=timezone.now()
        self.save()'''
    def approvedComment(self):
        self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})
    
    def __str__(self):
        return Post.title

class Comment(models.Model):
    post=models.ForeignKey('app_clone.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    text=models.CharField(max_length=1000)
    created_date=models.DateTimeField(default=timezone.now())
    approved_comments=models.BooleanField(default=False)

    def approve(self):
        Comment.approved_comments=True
        Comment.save()
    def get_absolute_url(self):
        return reverse('post_list')
    def __str__(self):
        return Comment.text

