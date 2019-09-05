"""Event App URLS"""
from django.urls import path
from .views import event_create_view, food_create_view

app_name = "events"

urlpatterns = [
    path("create/", event_create_view, name="event-create"),
    path("create/add_food/", food_create_view, name="food-add")
]
