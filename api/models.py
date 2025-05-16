import uuid
from django.db import models

class User_profile(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    handle = models.CharField(max_length=50, unique=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    @property
    def avatar_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return f"https://api.dicebear.com/9.x/micah/svg?seed={self.handle or self.email}"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='posts/')
    up_vote = models.PositiveIntegerField(default=0)
    down_vote = models.PositiveIntegerField(default=0)
    # comments = models.TextField(blank=True)
    created_by = models.ForeignKey(User_profile, on_delete=models.CASCADE, to_field='email', related_name='posts')
    description = models.TextField(blank=True)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")

    def __str__(self):
        return f"Post {self.id} by {self.created_by.email}"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User_profile, on_delete=models.CASCADE, to_field='email', related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.email} on {self.post.id}"