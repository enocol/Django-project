from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS = ((0, "Draft"), (1, "Published"))
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.CharField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body= models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_one = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
