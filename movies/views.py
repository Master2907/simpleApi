from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from .serializers import MovieModelSerializer
from .models import MovieModel

class GetMovie(APIView):

    def get(self, request, pk):
        query =  MovieModel.objects.get(id=pk)
        serialized = MovieModelSerializer(instance=query).data
        return Response(serialized)


