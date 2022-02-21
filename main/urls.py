from django.urls import path
from django.urls.resolvers import URLPattern
from main import views



urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/', views.News.as_view(), name='news-detail')
]