from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    video_id = models.IntegerField()
    thumbnail = models.ImageField(blank=True)

    def __str__(self):
        return self.movie_name

class User_Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username