from django.shortcuts import render
from django.views import generic
from movies.models import Genre, Movie
from inverted_index.query import get_search_result as inverted_index_search


class MovieListView(generic.ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        query_type = self.request.GET.get("query_type")
        select = self.request.GET.get("select")
        search = self.request.GET.get("search")
        if search and select:
            if query_type == 'django':
                if select == 'genres':
                    genre = Genre.objects.get(name=search)
                    object_list = self.get_queryset().filter(genres__in=[genre])
                else:
                    object_list = self.get_queryset().filter(**{f"{select}__icontains": search})

            context = super().get_context_data(**kwargs, object_list=object_list)
            context["search_term"] = search

            if query_type == 'inverted-index':
                if select == 'genres':
                    select = 'genre'
                context["inverted_index_search"] = True
                context["inverted_index_search_all"] = inverted_index_search("all", select, search)
                context["inverted_index_search_true"] = inverted_index_search("true", select, search)
            return context
        return super().get_context_data(**kwargs)

