from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Genre, Movie
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)

    context = {
        "movies":movies,
    }

    return render(request, 'movies/index.html', context)
    


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    context = {
        "movie":movie,
    }

    return render(request, 'movies/detail.html', context)
    


@require_safe
def recommended(request):
    pass
