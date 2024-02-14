from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/getmovie/<int:pk>', GetMovie.as_view()),
    path('api/getvideo/<int:pk>', GetVideo.as_view()),
]
