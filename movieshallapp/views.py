from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
from . models import HomeMovie,PopularMovies,UpcomingMovies,AddMovies,Review,Favourite,Genre
from .forms import AddMoviesForm,ReviewForm,CastForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def index(request):
    home=HomeMovie.objects.all()
    popular = PopularMovies.objects.all()
    upcoming = UpcomingMovies.objects.all()
    return render(request,'index.html',{'home':home,'popular':popular,'upcoming':upcoming})

def addmovies(request):
    if request.method == 'POST':
        form = AddMoviesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movieshallapp:mymovies')
    else:
        form = AddMoviesForm()
    return render(request,'addmovies.html',{'form':form})

def addcast(request):
    if request.method == 'POST':
        form = CastForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movieshallapp:addmovies')
    else:
        form = CastForm()
    return render(request,'addcast.html',{'form':form})

def mymovies(request):
    movies = AddMovies.objects.all()
    return render(request,'mymovies.html',{'movies':movies})

def movie_details(request,id):
    movie = get_object_or_404(AddMovies,id=id)
    movie_added_to_favourites = Favourite.objects.filter(user=request.user,movie=movie).exists()
    review_form = ReviewForm()
    user_review = Review.objects.filter(movie=movie,user=request.user).first()
    other_reviews = Review.objects.filter(movie=movie).exclude(user=request.user)
    if request.method == 'POST':
        if 'review' in request.POST:
            review_form = ReviewForm(request.POST,instance=user_review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                return redirect('movieshallapp:movie_details',id=id)
    else:
        review_form = ReviewForm(instance=user_review)
    return render(request,'movie_details.html',{'movie':movie,'review_form':review_form,'user_review':user_review,
                                                'other_reviews':other_reviews,'movie_added_to_favourites': movie_added_to_favourites})

def update_movie(request,id):
    movies = get_object_or_404(AddMovies,id=id)
    if movies.added_by != request.user:
        return HttpResponseForbidden("You are not authorized to update this movie.")
    if request.method == 'POST':
        form = AddMoviesForm(request.POST,request.FILES,instance=movies)
        if form.is_valid():
            form.save()
            return redirect('movieshallapp:mymovies')
    else:
        form = AddMoviesForm(instance=movies)
    return render(request,'update.html',{'form':form,'movies':movies})

def delete_movie(request,id):
    movies = get_object_or_404(AddMovies,id=id)
    if movies.added_by != request.user:
        return HttpResponseForbidden("You are not authorized to delete this movie.")
    if request.method == 'POST':
        movies = AddMovies.objects.get(id=id)
        movies.delete()
        return redirect('movieshallapp:mymovies')
    # return render(request,'delete_movie.html',{'movies':movies})

def search_movies(request):
    query = None
    query = request.GET.get('query')
    if query:
        movies = AddMovies.objects.all().filter(title__icontains=query)
    else:
        movies = []
    return render(request,'movie_search.html',{'movies':movies})


def add_to_favourites(request,id):
    if request.method == 'POST':
        movie = get_object_or_404(AddMovies,id=id)
        favourite, created = Favourite.objects.get_or_create(user=request.user,movie=movie)
        if created:
            messages.success(request,'Movie added to favourites')
        else:
            messages.error(request,'Movie is already in favourites')
    return redirect('movieshallapp:movie_details',id=id)

def favourites(request):
    favourites = Favourite.objects.filter(user=request.user)
    return render(request, 'favourites.html', {'favourites': favourites})

def genre(request):
    selected_genre = request.GET.get('genre')
    query = request.GET.get('query')
    genres = Genre.objects.all()
    if query:
        movies = AddMovies.objects.filter(genre__name__icontains=query)
    elif selected_genre and selected_genre != 'All':
        movies = AddMovies.objects.filter(genre__name=selected_genre)
    else:
        movies = AddMovies.objects.all()
    context = {
        'genres': genres,
        'selected_genre': selected_genre,
        'movies': movies,
    }
    return render(request,'genre.html',context)

# def update_movie(request,id):
#     movies = AddMovies.objects.get(id=id)
#     form = AddMovies(request.POST or None, request.FILES,instance=movies)
#     if form.is_valid():
#         form.save()
#         return redirect('movieshallapp:mymovies')
#     return render(request, 'update.html', {'form': form, 'movies': movies})
#def search_movies(request):
#     movies = None
#     query = None
#     if 'q' in request.GET:
#         query = request.GET.get('q')
#         movies = AddMovies.objects.all().filter(Q(title__contains=query))
#         return render(request,'movie_search.html',{'query':query,'movies':movies})

# def movie_details(request,id):
#     movies = get_object_or_404(AddMovies,id=id)
#     return render(request,'movie_details.html',{'movies':movies})
