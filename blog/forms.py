from .models import Comment, Post
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'status', 'excerpt', 'featured_image')