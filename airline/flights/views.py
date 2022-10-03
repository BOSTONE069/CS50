from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Airport, Passenger


# Create your views here.
def index(request):
    """
    It takes a request, renders the index.html template, and passes in a dictionary with a key of flights and a value of
    Flight.objects.all()

    :param request: The request object is the first parameter to every view. It contains information about the request that
    was made to the server
    :return: The index.html file is being returned.
    """
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    """
    It gets a flight by its primary key, and then renders a template called `flights/flight.html` with the flight and its
    passengers

    :param request: The request object is the first parameter to any view. It contains information about the current
    request, such as the method (GET or POST), the user (if any), and the GET and POST parameters
    :param flight_id: This is the name of the parameter that will be passed to the view
    :return: The flight and the passengers on the flight.
    """
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))