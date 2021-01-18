from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag (models.Model):
    tag = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.tag

class Image (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pic = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    tags = models.ManyToManyField(Tag)
    public = models.BooleanField(default=True)
    def __str__(self):
        return self.name

