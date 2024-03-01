from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all().order_by("-created_on").filter(status=1)  
    template_name = "blog/index.html"
    paginate_by = 6



# def post_detail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, "blog/post_detail.html", {"post": post})


def post_detail(request, id):
    queryset = Post.objects.all().order_by("-created_on")
    post = get_object_or_404(queryset, id=id)
    context={"post": post,
             "coder": "Enoh C",}

    return render(
        request,
        "blog/post_detail.html",
        context
    )