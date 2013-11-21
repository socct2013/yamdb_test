from django.shortcuts import render

from movies.models import Movie, Actor


def index(request):
    movie_list = Movie.objects.all()
    return render(request, 'movies/index.html', {'movie_list': movie_list})