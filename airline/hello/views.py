from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def boston(request):
    return HttpResponse("Hello Bostone")


def greetings(request, name):
    return render(request, "hello/greetings.html", {
       "name": name.capitalize()
    })
