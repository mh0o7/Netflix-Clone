from django.db import models

class Generics(models.Model):
    type = models.CharField(max_length=100)
    description = models.CharField(null=True)
    subgeners = models.CharField()
    example  = models.CharField()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    poster = models.ImageField()
    trailer = models.FileField(null=True)
    release_date  = models.DateTimeField()
    description = models.TextField()
    rating = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    generics= models.OneToOneField(Generics, on_delete=models.CASCADE)  
    duration  = models.IntegerField()
    country = models.CharField(max_length=100)
    language = models.CharField() 
    country = models.CharField()
    created_at = models.DateTimeField()
    updated_at =  models.DateTimeField()

class Series(models.Model):
    title = models.CharField(max_length=100)
    realease_date = models.DateTimeField()
    season_number = models.IntegerField()
    episode_number =  models.IntegerField()
    episode_name = models.CharField(max_length=100)
    episode_description = models.CharField(max_length=100)
    generics  = models.OneToOneField(Generics)
    rating = models.FloatField(null=True)
    country = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at =  models.DateTimeField()


    
