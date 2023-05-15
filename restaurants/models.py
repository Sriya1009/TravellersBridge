from django.db import models
from django.urls import reverse

class Reservation(models.Model):
    app_label = 'restaurants'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('restaurants:booking_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.name} - {self.restaurant.name} - {self.date} {self.time}"

class Restaurant(models.Model):
    app_label = 'restaurants'
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
