from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date  = models.DateTimeField()
    description = models.TextField()
    rating = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    genres = models.JSONField()
    runtime = models.IntegerField()
    country = models.CharField(max_length=100)


class Series(models.Model):
    title = models.CharField(max_length=100)
    realease_date = models.DateTimeField()
    season_number = models.IntegerField()
    episode_number =  models.IntegerField()
    episode_name = models.CharField(max_length=100)
    episode_name = models.CharField(max_length=100)
    episode_description = models.CharField(max_length=100)
    rating = models.FloatField()
    country = models.CharField(max_length=10)
    


    

