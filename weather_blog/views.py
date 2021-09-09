from rest_framework import generics, serializers
from .serializers import WeatherBlogSerializer
from .models import Weather_blog

class WeatherBlogList(generics.ListCreateAPIView):
  queryset = Weather_blog.objects.all()
  serializer_class = WeatherBlogSerializer

class WeatherBlogDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Weather_blog.objects.all()
  serializer_class = WeatherBlogSerializer
