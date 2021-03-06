from django.db import models
import uuid


# Project Main Object
class Project(models.Model):
    title = models.CharField(max_length=200)
    unique_id = models.UUIDField(default=uuid.uuid4,
                                 editable=False, unique=True)
    description = models.TextField(max_length=500)
    zipFile = models.CharField(max_length=500)
    remoteFile = models.ForeignKey('RemoteFile', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# RemoteFile to Project Object (o2o)
class RemoteFile(models.Model):
    name = models.CharField(max_length=200)
    fileType = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    content = models.TextField(max_length=200000)

    def __str__(self):
        return self.name


# Key Object for Download and RemoteFile
class Key(models.Model):
    uniqueKey = models.UUIDField(default=uuid.uuid4,
                                 editable=False, unique=True)
    fullname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.email
