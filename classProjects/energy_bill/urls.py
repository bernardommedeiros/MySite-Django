from django.urls import path
from . import views

urlpatterns = [
    path('', views.energy, name='energy'),
     path('result/', views.bill_calculate_result, name='bill_calculate'),
]
