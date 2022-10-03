from django.contrib import admin

from .models import Flight, Airport, Passenger


# Register your models here.
# When I visit the admin page for flights, I want to see the origin, destination, and duration columns.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin", "destination", "duration")


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


class AirportAdmin(admin.ModelAdmin):
    list_display = ("code", "city")


admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
