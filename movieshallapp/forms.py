from django import forms
from .models import AddMovies,Review,Cast

# class AddMoviesForm(forms.ModelForm):
#     class Meta:
#         model=AddMovies
#         fields=['title','poster_img','description','release_date','genre','youtube_link','actor1','actor1_img',
#                 'actor2','actor2_img','actor3','actor3_img','actor4','actor4_img','actor5','actor5_img',]

class AddMoviesForm(forms.ModelForm):
    class Meta:
        model = AddMovies
        fields = ['title','poster_img','description','release_date','genre','youtube_link','casts',
                'duration','added_by','director_name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']

class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = ['name','img']
