from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<pk>/', views.DetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<pk>/edit/',views.UpdatePostView.as_view(),name='post_edit'),
    path('post/<pk>/remove/',views.DeleatPostView.as_view(),name='post_remove'),
    path('draft/',views.DraftListView,name='post_draft_list'),
    
]
