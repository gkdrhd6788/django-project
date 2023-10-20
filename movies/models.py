from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    content = models.TextField()
    