from django.urls import path
from . import views

app_name='movieshallapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('addmovies/',views.addmovies,name='addmovies'),
    path('mymovies/',views.mymovies,name='mymovies'),
    path('mymovies/<int:id>/',views.movie_details,name='movie_details'),
    path('mymovies/<int:id>/update/',views.update_movie,name='update_movie'),
    path('mymovies/<int:id>/delete/',views.delete_movie,name='delete_movie'),
    path('mymovies/search/',views.search_movies,name='search_movies'),
    path('add_to_favourites/<int:id>/',views.add_to_favourites,name='add_to_favourites'),
    path('favourites/',views.favourites,name='favourites'),
    path('genre/',views.genre,name='genre'),
    path('addcast/',views.addcast,name='addcast'),
    # path('genre/',views.genre,name='genre'),
]