from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]

admin.site.site_header = 'Flight Administration Site'    # default: "Django Administration"
admin.site.index_title = 'Flight, Airports and Passenger'                 # default: "Site administration"
admin.site.site_title = 'HTML title from administration' # default: "Django site admin"