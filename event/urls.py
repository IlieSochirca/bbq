"""Event App URLS"""
from django.urls import path
from .views import event_create_view, food_create_view, drinks_create_view, events_list_view, event_detail_view, \
    accept_invite_view

app_name = "events"

urlpatterns = [
    path("", events_list_view, name="events-list"),
    path("<int:pk>", event_detail_view, name="event-detail"),
    path("<int:pk>/invite/<uuid:invite_pk>/", accept_invite_view, name="accept-invitation-view"),
    path("create/", event_create_view, name="event-create"),
    path("create/add_food/", food_create_view, name="food-add"),
    path("create/add_drinks/", drinks_create_view, name="drinks-add"),
]
