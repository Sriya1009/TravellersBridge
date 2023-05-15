from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation, Restaurant
from .forms import ReservationForm

def index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})

def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.restaurant = form.cleaned_data['restaurant']
            reservation.save()
            return redirect('restaurants:booking_detail', pk=reservation.pk)
    else:
        form = ReservationForm()
    return render(request, 'restaurants/book_table.html', {'form': form})

def booking_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'restaurants/booking_list.html', {'reservations': reservations})

def booking_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'restaurants/booking_detail.html', {'reservation': reservation})

def booking_edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.restaurant = form.cleaned_data['restaurant']
            reservation.save()
            return redirect('restaurants:booking_detail', pk=reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'restaurants/book_table.html', {'form': form})

def booking_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('restaurants:booking_list')
    return render(request, 'restaurants/booking_confirm_delete.html', {'reservation': reservation})
