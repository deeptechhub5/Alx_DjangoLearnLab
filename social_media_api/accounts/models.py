from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    return f'profile_pictures/user_{instance.id}/{filename}'

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    # Users that THIS user follows
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username
