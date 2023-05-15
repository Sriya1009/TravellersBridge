from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.search_flights, name='search_flights'),
]
