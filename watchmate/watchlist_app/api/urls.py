from django.urls import path
# from .views import movie_list, movie_details
from .views import movieListAV, movieDetailsAV

urlpatterns = [
    path('', movieListAV.as_view(), name='Movie List'),
    path('<int:pk>/', movieDetailsAV.as_view(), name='Movie'),
]
