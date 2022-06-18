# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Movie


# def movie_list(req):
#     movies = Movie.objects.all()
#     response = {
#         'message': 'Fetched succesfully',
#         'movies': list(movies.values())
#     }
#     return JsonResponse(response)


# def movie_details(req, pk):
#     movie = Movie.objects.get(pk=pk)
#     response = {
#         'message': 'Fetched succesfully',
#         'name': movie.name,
#         'description': movie.description,
#         'is_active': movie.is_active
#     }
#     return JsonResponse(response)
