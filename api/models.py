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
