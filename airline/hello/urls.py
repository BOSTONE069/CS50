from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greetings, name="greet"),
    path("boston", views.boston, name="boston")
]
