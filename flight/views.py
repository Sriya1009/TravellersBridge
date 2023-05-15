from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Flight

def search_flights(request):
    if request.method == 'POST':
        source = request.POST.get('from-place')
        departure_date = request.POST.get('date-start')
        return_date = request.POST.get('date-end')
        
        # Perform flight search based on the input parameters
        flights = Flight.objects.filter(source=source, departure_date=departure_date, return_date=return_date)
        
        context = {'flights': flights}
        return render(request, 'searchflight.html', context)
    
    return render(request, 'searchflight.html')

def search_flights(request):
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        flight_class = request.POST.get('flight_class')
        source = request.POST.get('from-place')
        adults = int(request.POST.get('adults'))
        children = int(request.POST.get('children'))

        # Perform the flight search based on the criteria
        flights = Flight.objects.filter(
            date__gte=check_in,
            date__lte=check_out,
            available_seats__gte=(adults + children)
        )

        return render(request, 'flights/search_results.html', {'flights': flights})

    return render(request, 'flights/search_flights.html')