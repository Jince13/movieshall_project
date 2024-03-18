from django.contrib import admin
from . models import HomeMovie,PopularMovies,UpcomingMovies,Genre,AddMovies,Cast
# Register your models here.
admin.site.register(HomeMovie)
admin.site.register(PopularMovies)
admin.site.register(UpcomingMovies)
admin.site.register(AddMovies)
admin.site.register(Cast)
admin.site.register(Genre)

