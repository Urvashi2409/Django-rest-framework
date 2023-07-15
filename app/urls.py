from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.MovieList.as_view(), name='movie_list'),
    path('movie/<int:pk>', views.MovieDetails.as_view(), name='movie_details'),
    # path('movie/', views.movie_list),
    # path('movie/<int:pk>', views.movie_details),
]
