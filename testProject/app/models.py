from django.db import models
from tinymce.models import HTMLField

class User(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField(max_length= 50)
    comment = HTMLField()

    def __str__(self):
        return self. name
