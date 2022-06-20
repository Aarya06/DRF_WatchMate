from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import WatchlistSerializer, StreamingPlatformSerializer, ReviewSerializer
from ..models import WatchList, StreamingPlatform, Review
from rest_framework import status, generics

# VIEWS USING GENERIC VIEW
    
class ReviewListGV(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # OVERWITE QUERYSET METHOD
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    # OVERWITE CREATE METHOD
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        
        serializer.save(watchlist=watchlist)
    
class ReviewGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# # VIEWS USING MIXINS    
# class ReviewListGV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ReviewGV(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

class WatchListAV(APIView):

    def get(self, req):
        list = WatchList.objects.all()
        serializer = WatchlistSerializer(list, many=True)
        return Response(serializer.data)

    def post(self, req):
        serializer = WatchlistSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailsAV(APIView):

    def get(self, req, pk):
        try:
            item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(item)
        return Response(serializer.data)

    def put(self, req, pk):
        try:
            item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(item, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        try:
            item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
    
class StreamingPlatformAV(APIView):

    def get(self, req):
        list = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(list, many=True)
        return Response(serializer.data)

    def post(self, req):
        serializer = StreamingPlatformSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamingPlatformDetailsAV(APIView):

    def get(self, req, pk):
        try:
            item = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamingPlatformSerializer(item)
        return Response(serializer.data)

    def put(self, req, pk):
        try:
            item = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamingPlatformSerializer(item, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        try:
            item = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)

# # DRF CLASS BASED VIEWS

# class movieListAV(APIView):

#     def get(self, req):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, req):
#         serializer = MovieSerializer(data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class movieDetailsAV(APIView):

#     def get(self, req, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def put(self, req, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, req, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)


# DRF FUNCTION BASED VIEWS

# @api_view(["GET", "POST"])
# def movie_list(req):
#     if req.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if req.method == 'POST':
#         serializer = MovieSerializer(data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def movie_details(req, pk):
#     if req.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if req.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if req.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
