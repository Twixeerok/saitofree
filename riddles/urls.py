from django.urls import path
from django.urls.resolvers import URLPattern
from riddles import views
from .import views


urlpatterns = [
    path('', views.index, name='lol'),
    path('riddles/', views.index),
    path('<int:pk>/', views.News.as_view(), name='news-detail')
]