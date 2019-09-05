from django.shortcuts import render, redirect

from .forms import EventForm, FoodForm
from .models import Event


# Create your views here.


def event_create_view(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }

    return render(request, "events/event_create.html", context=context)


# def event_detail_view(request):


def food_create_view(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("event-create")

    context = {
        "form": form
    }

    return render(request, "events/food_create.html", context=context)
