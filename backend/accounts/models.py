from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

# Create your models here.
def profile_image_path(instance, filename):
    return f'profile/{instance.username}/{filename}'

def backdrop_image_path(instance, filename):
    return f'backdrop/{instance.username}/{filename}'

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical = False, related_name = 'followers')
    score = models.IntegerField(default=0)
    profile_image = models.ImageField(default='/profile/default.png', blank=True, upload_to=profile_image_path)
    backdrop_image = models.ImageField(default='/backdrop/default.jpg', blank=True, upload_to=backdrop_image_path)
