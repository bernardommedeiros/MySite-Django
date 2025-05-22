from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan, name='loan'),
    path('result/', views.loan_calculate_result, name='loan_calculate'),
]