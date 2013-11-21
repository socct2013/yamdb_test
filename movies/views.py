from django.shortcuts import render, Http404

from movies.models import Movie, Actor


def index(request):
    movie_list = Movie.objects.all()
    return render(request, 'movies/index.html', {'movie_list': movie_list})


def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404
    return render(request, 'movies/movie_details.html', {'movie': movie})


def actor_detail(request, actor_id):
    try:
        actor = Actor.objects.get(pk=actor_id)
        formatted_name = actor.full_name('lfmi')
    except Actor.DoesNotExist:
        raise Http404
    return render(request, 'movies/actor_details.html', {'actor': actor,
                                                         'formatted_name': formatted_name})