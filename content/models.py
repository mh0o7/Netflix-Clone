from enum import unique
from django.db import models

class Movie(models.Model):
    tmdb_id = models.interField(unique=True)
    name = models.CharField(max_length=100)
    release_date  = models.DateTimeField()
    description = models.TextField()
    ratinng = models.FloatField()







class Series(models.Model):
    title = models.CharField(max_length=100)


