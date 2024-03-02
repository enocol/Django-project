from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.contrib import messages


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
    comments = post.comments.filter(approved=True) 

    
    comment_form = CommentForm()
    context={"post": post,
             "coder": "Enoh C",
             "comments": comments,
             "comment_form": comment_form,}
    
    if request.method == "POST":
       comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

    return render(
        request,
        "blog/post_detail.html",
        context
    )

