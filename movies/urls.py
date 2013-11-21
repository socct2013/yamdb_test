from django.conf.urls import patterns, url

from movies import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>\d+)/$', views.movie_detail, name='movie_detail'),
    url(r'^actor/(?P<actor_id>\d+)/$', views.actor_detail, name='actor_detail'),
)