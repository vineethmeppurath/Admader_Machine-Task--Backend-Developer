from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TagModel(models.Model):
    title = models.CharField(max_length=100,unique=True)

class SnippetModel(models.Model):
    text = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(TagModel, default=0, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)

