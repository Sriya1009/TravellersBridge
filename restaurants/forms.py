from django import forms
from .models import Reservation
from .models import Restaurant
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

