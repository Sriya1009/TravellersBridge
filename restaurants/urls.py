from django.contrib import admin
from django.urls import path
from . import views

app_name = 'restaurants'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_table/', views.book_table, name='book_table'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('booking_detail/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('booking_edit/<int:pk>/', views.booking_edit, name='booking_edit'),
    path('booking_delete/<int:pk>/', views.booking_delete, name='booking_delete'),
]


