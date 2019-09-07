import uuid

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from bbq import settings
from .forms import EventForm, FoodForm, DrinksForm, AcceptInvitationForm
from .models import Event, Attendee


@login_required()
def event_create_view(request):
    """
    Event Create Function Based view
    :param request:
    :return:
    """
    template_name = "events/event_create.html"
    form = EventForm(request.POST or None)
    if form.is_valid():
        inst = form.save(commit=False)
        inst.organizer = request.user
        inst.save()
        public_url = f"{settings.DOMAIN}events/{inst.pk}/invite/{uuid.uuid4()}"
        inst.public_invite_url = public_url
        inst.save()
        inst.food.add(form.cleaned_data["food"])
        inst.drinks.add(form.cleaned_data["drinks"])
        inst.save()
        return redirect(reverse("events:events-list"))
    context = {
        "form": form
    }

    return render(request, template_name, context=context)


def events_list_view(request):
    """
    Events list Function Based view
    :param request:
    :return:
    """
    template_name = "events/events_list.html"
    queryset = Event.objects.filter(organizer=request.user)
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


def event_detail_view(request, pk):
    """
    Event Detail Function Based View
    :param request:
    :param pk:
    :return:
    """
    template_name = "events/event_details.html"
    event = get_object_or_404(Event, pk=pk)
    event_food = event.food.all()
    event_drinks = event.drinks.all()
    attendees_names = Attendee.objects.filter(event=pk)
    total_no_attendees = attendees_names.count() + event.no_guests
    context = {
        "event": event,
        "event_food": event_food,
        "event_drinks": event_drinks,
        "attendees_names": attendees_names,
        "total_no_attendees": total_no_attendees
    }
    return render(request, template_name, context)


def food_create_view(request):
    """
    Create Food View
    :param request:
    :return:
    """
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse("events:event-create"))

    context = {
        "form": form
    }

    return render(request, "events/food_create.html", context=context)


def drinks_create_view(request):
    """
    Drinks Create View
    :param request:
    :return:
    """
    form = DrinksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse("events:event-create"))

    context = {
        "form": form
    }
    return render(request, "events/drink_create.html", context=context)


def accept_invite_view(request, pk, invite_pk):
    """
    Accept Invite View
    :param request:
    :param pk:
    :param invite_pk:
    :return:
    """
    template_name = "events/accept_invite.html"
    event = get_object_or_404(Event, pk=pk)
    event_food = event.food.all()
    event_drinks = event.drinks.all()
    form = AcceptInvitationForm(event, request.POST or None)
    if form.is_valid():
        inst = form.save(commit=True)
        event.no_guests += int(request.POST["no_guests"])
        event.save()
        inst.event.add(event)
        inst.save()
        return redirect(reverse("events:event-details", kwargs={"pk": pk}))
    context = {
        "form": form,
        "event": event,
        "event_food": event_food,
        "event_drinks": event_drinks,
    }
    return render(request, template_name, context=context)
