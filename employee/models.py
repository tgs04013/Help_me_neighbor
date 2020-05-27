from django.db import models

# Create your models here.
class Article(models.Model):
    author      = models.CharField(max_length=120)
    title       = models.CharField(max_length=120)
    text        = models.TextField()
    password    = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title