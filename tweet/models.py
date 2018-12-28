from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Tweet(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField('date published', default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
