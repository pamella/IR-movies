from django.urls import path
from movies.views import MovieListView


app_name = 'movies'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),

]
