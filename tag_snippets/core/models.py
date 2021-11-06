from django.db import models

# Create your models here.
class TagModel(models.Model):
    title = models.CharField(max_length=100,unique=True)

class SnippetModel(models.Model):
    text = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
