from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('post/<int:pk>/delete/', views.delete_comment, name='delete_comment')
]