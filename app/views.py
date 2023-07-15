from app.serializers import MovieSerializer
from .models import Movie
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class MovieList(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serialized = MovieSerializer(movies, many=True)
        return Response(serialized.data)
    
    def post(self, request):
        serialized = MovieSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetails(APIView):

    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serialized = MovieSerializer(movie)
        return Response(serialized.data)
    
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serialized = MovieSerializer(movie, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serialized = MovieSerializer(movies, many=True)
#         return Response(serialized.data)

#     elif request.method == 'POST':
#         serialized = MovieSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serialized = MovieSerializer(movie)
#         return Response(serialized.data)
    
#     elif request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serialized = MovieSerializer(movie, data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
        
#     elif request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)