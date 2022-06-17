from distutils import text_file
from django.conf import settings
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField((""))
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(auto_now_add=True)