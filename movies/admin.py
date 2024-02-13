from django.contrib import admin
from .models import MovieModel
# Register your models here.

@admin.register(MovieModel)
class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'genres', 'description']
    list_filter = ['id', 'year']