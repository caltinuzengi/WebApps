from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Media(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="static/img/")
    type = models.CharField(max_length= 100)
    genre = models.CharField(max_length= 100)
    homepage = models.BooleanField(default = True)