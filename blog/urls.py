from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/', views.comment_edit, name='comment_edit'),
    path('post/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('add_post/', views.add_post, name='addpost'),
]