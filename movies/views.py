from django.shortcuts import render
from django.views import generic
from movies.models import Genre, Movie


class MovieListView(generic.ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        select = self.request.GET.get("select")
        search = self.request.GET.get("search")
        if search and select:
            object_list = self.get_queryset().filter(**{f"{select}__iexact": search})
            context = super().get_context_data(**kwargs, object_list=object_list)
            context["search_term"] = search
            return context
        return super().get_context_data(**kwargs)

