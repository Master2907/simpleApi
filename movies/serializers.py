from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import MovieModel

class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieModel
        fields = '__all__'

class MovieVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model=MovieModel
        fields = ['id', 'video']