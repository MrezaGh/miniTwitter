from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TokenV1(models.Model):
    key = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.key


class TokenV2(models.Model):
    key = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.key
