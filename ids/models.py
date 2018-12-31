from django.db import models
from django.utils import timezone



# Create your models here.
class AnonymousUser(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    repeatedUnauthorized = models.IntegerField(default=0)  # number of repeated requests that was unauthorized
    fastRequestChain = models.IntegerField(default=0)  # number of repeated requests with a little time between them
    lastRequestTimeStamp = models.IntegerField(default=timezone.now().timestamp())

    def __str__(self):
        return self.pk


class RequestInfo(models.Model):
    anonymousUser = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE)
    browser = models.CharField(max_length=200)
    timeStamp = models.IntegerField()

    def __str__(self):
        return 'user ip: ' + self.anonymousUser.pk + ' *** timeStamp: ' + str(self.timeStamp)


class LogInTable(models.Model):
    myip = models.IntegerField(primary_key=True)
    mysession = models.CharField(max_length=40)

    def __str__(self):
        return self.myip
