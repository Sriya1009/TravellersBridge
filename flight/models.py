from django.db import models


from django.db import models

class Flight(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    source=models.CharField(max_length=100)
    available_seats = models.PositiveIntegerField()
    flight_class=models.

    def __str__(self):
        return f"{self.departure} to {self.destination} - {self.date}"
