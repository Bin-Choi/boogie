from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


# Create your models here.
def profile_image_path(instance, filename):
    return f'profile/{instance.username}/{filename}'

def backdrop_image_path(instance, filename):
    return f'backdrop/{instance.username}/{filename}'
    
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical = False, related_name = 'followers')
    score = models.IntegerField(default=0)
    # profile_image = models.ImageField(default='/profile/default.png', blank=True, upload_to=profile_image_path)
    profile_image = ProcessedImageField(
        blank=True, 
        default='profile/default.png', 
        upload_to=profile_image_path,
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={'quality': 80},
        )
    # backdrop_image = models.ImageField(default='/backdrop/default.jpg', blank=True, upload_to=backdrop_image_path)
    backdrop_image = ProcessedImageField(
        blank=True, 
        default='backdrop/default.jpg', 
        upload_to=backdrop_image_path,
        processors=[ResizeToFill(1200, 600)],
        format='JPEG',
        options={'quality': 80},
        )
    adventure = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    drama = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    western = models.IntegerField(default=0)
    thriller = models.IntegerField(default=0)
    crime = models.IntegerField(default=0)
    documentary = models.IntegerField(default=0)
    science_fiction = models.IntegerField(default=0)
    mystery = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    tv_movie = models.IntegerField(default=0)