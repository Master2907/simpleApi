from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.http import Http404

from .serializers import MovieModelSerializer, MovieVideoSerializer
from .models import MovieModel

class GetMovie(APIView):

    def get(self, request, pk):
        try:
            query =  MovieModel.objects.get(id=pk)
            serialized = MovieModelSerializer(instance=query).data
            return Response(serialized)
        except: 
            raise Http404


class GetVideo(APIView):

    def get(self, request, pk):
        try:
            query =  MovieModel.objects.get(id=pk)
            serialized = MovieVideoSerializer(instance=query).data
            return Response(serialized)
        except: 
            raise Http404