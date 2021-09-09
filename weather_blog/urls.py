from django.urls import path
from .views import WeatherBlogList, WeatherBlogDetail

urlpatterns = [
    path('', WeatherBlogList.as_view(), name='weatherblog_list'),
    path('<int:pk>/', WeatherBlogDetail.as_view(), name='weatherblog_detail')
]
