from django.urls import path
from .views import movie_list, movie_details
urlpatterns = [
    path('',movie_list, name='Movie List'),
    path('<int:pk>/',movie_details, name='Movie'),
]
