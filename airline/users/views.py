from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))


def login(request):
    return render(request, "users/login.html")


def logout(request):
    return render(request, "users/logout.html")