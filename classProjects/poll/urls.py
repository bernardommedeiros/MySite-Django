from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_select, name='poll_select'),
      path('vote_result/', views.vote_result, name='vote_result'),
    path('ranking/', views.ranking, name='ranking'),
]