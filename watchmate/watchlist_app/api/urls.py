from django.urls import path
# from .views import movie_list, movie_details
from .views import WatchListAV, WatchListDetailsAV, StreamingPlatformAV, StreamingPlatformDetailsAV

urlpatterns = [
    path('', WatchListAV.as_view(), name='Watch List'),
    path('<int:pk>/', WatchListDetailsAV.as_view(), name='Item Details'),
    path('stream/', StreamingPlatformAV.as_view(), name='Streaming Platform List'),
    path('stream/<int:pk>/', StreamingPlatformDetailsAV.as_view(), name='Streaming Platform Details'),
]
