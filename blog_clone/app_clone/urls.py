from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<pk>/', views.DetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<pk>/edit/',views.UpdatePostView.as_view(),name='post_edit'),
    path('post/<pk>/remove/',views.DeleatPostView.as_view(),name='post_remove'),
    path('post/<pk>/publish/',views.publish_post,name='post_publish'),
    path('draft/',views.DraftListView,name='post_draft_list'),

    path('post/<pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<pk>/remove/',views.comment_remove,name='comment_remove'),
    
    
]
