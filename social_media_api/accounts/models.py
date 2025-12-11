from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/profile_pictures/user_<id>/<filename>
    return f'profile_pictures/user_{instance.id}/{filename}'

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    # followers: users who follow this user (directional)
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username
