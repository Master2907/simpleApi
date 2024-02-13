from django.db import models

from config.helpers import convert_file_name, convert_poster_name
from datetime import datetime

age_choices = (
    ('4+', '4+'),
    ('12+', '12+'),
    ('16+', '16+'),
    ('18+', '18+'),
)

class MovieModel(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=datetime.now().year)
    description = models.TextField()
    genres = models.TextField()
    poster = models.ImageField(upload_to=convert_poster_name)
    video = models.FileField(upload_to=convert_file_name)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'