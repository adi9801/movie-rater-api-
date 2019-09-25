from django.contrib import admin
from .models import Movie, Rating
# Register your models here.
# admin.site.register(Movie)
# admin.site.register(Rating)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'stars']
    list_filter = ['movie', 'user', 'stars']
    search_fields = ['movie', 'user', 'stars']