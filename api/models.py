from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User_profile(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    handle = models.CharField(max_length=50, unique=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"