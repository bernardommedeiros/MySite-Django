from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_select, name='poll_select'),
    path('ranking/', views.ranking, name='ranking'),
]