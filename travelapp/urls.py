from django.contrib import admin
from django.urls import include, path
from travelapp.apps import TravelappConfig

urlpatterns = [
    path('admin/', admin.site.urls)
]