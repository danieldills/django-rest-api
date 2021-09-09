from rest_framework import serializers
from .models import Weather_blog

class WeatherBlogSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'author', 'title', 'body', 'created_at')
    model = Weather_blog
