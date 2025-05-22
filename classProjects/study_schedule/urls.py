from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('result/', views.schedule_generate_result, name='schedule_generate'),
]