from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages


# Create your views here.
class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all().order_by("-created_on").filter(status=1)  
    template_name = "blog/index.html"
    paginate_by = 6



def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all() 

    
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
    return render(request, "blog/post_detail.html", context)


def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.approved = False
            comment.save()
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form})


def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Comment deleted successfully'
    )
    return redirect('post_detail', slug=comment.post.slug)
    # return HttpResponseRedirect(reverse('post_detail', args=[comment.post.slug]))



