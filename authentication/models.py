from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Avatar(models.Model):

    image = models.ImageField(upload_to='authentication/images/')  # todo
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
