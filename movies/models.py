from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256, )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=256, )
    url = models.URLField(max_length=256, )
    genres = models.ManyToManyField('movies.Genre', related_name='movies')
    year = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    director = models.CharField(max_length=256, blank=True, null=True)
    studio = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

