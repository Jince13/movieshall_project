import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class HomeMovie(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics/home_img')
    youtube_link = models.URLField()

    def __str__(self):
        return self.title

class PopularMovies(models.Model):
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics/popular_movies_img')
    youtube_link = models.URLField()

    def __str__(self):
        return self.title

class UpcomingMovies(models.Model):
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics/upcoming_movies_img')
    release_date = models.CharField(max_length=250)
    youtube_link = models.URLField()

    def __str__(self):
        return self.title

class AddMovies(models.Model):
    title = models.CharField(max_length=130)
    poster_img = models.ImageField(upload_to='pics/added_movies_img')
    description = models.CharField(max_length=130)
    release_date = models.CharField(max_length=130)
    genre = models.ManyToManyField('Genre',related_name='movies')
    youtube_link = models.URLField()
    casts = models.ManyToManyField('Cast',related_name='movies')
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)
    duration = models.CharField(max_length=130)
    director_name = models.CharField(max_length=130)
    # actor1 = models.CharField(max_length=130)
    # actor1_img = models.ImageField(upload_to='pics/cast_img')
    # actor2 = models.CharField(max_length=130)
    # actor2_img = models.ImageField(upload_to='pics/cast_img')
    # actor3 = models.CharField(max_length=130)
    # actor3_img = models.ImageField(upload_to='pics/cast_img')
    # actor4 = models.CharField(max_length=130)
    # actor4_img = models.ImageField(upload_to='pics/cast_img')
    # actor5 = models.CharField(max_length=130)
    # actor5_img = models.ImageField(upload_to='pics/cast_img')

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Cast(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics/cast_img')

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(AddMovies,on_delete=models.CASCADE,related_name='review')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.CharField(max_length=250)

class Favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(AddMovies,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')