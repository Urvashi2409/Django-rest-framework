from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.WatchListView.as_view(), name='watchlist'),
    path('movie/<int:pk>', views.WatchListDetailView.as_view(), name='watchlist_details'),
    # path('movie/', views.movie_list),
    # path('movie/<int:pk>', views.movie_details),
]
