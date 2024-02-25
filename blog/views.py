from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")    
    template_name = "post_list.html"


# def post_data(request):
#     template_name = "post.html"
#     post = Post.objects.all()
#     context = {"posts": post}
#     return render(request, template_name, context)   