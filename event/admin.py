from django.contrib import admin
from .models import Event, Food, Drink, Attendee

# Register your models here.

admin.site.register(Event)
admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(Attendee)
