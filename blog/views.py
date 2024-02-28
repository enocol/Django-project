from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all().order_by("-created_on")    
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6



# def post_detail(request, slug):
#     post = Post.objects.get(slug=slug)
#     return render(request, "blog/post_detail.html", {"post": post})


def post_detail(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )