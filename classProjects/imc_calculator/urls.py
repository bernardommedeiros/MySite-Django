from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_imc, name='form_imc'),
    path('result/', views.imc_calculate, name='imc_calculate'),
]
