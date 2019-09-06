import uuid

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from bbq import settings
from .forms import EventForm, FoodForm, DrinksForm, AcceptInvitationForm
from .models import Event, Attendee, Food, Drink


# Create your views here.

@login_required()
def event_create_view(request):
    template_name = "events/event_create.html"
    form = EventForm(request.POST or None)
    if form.is_valid():
        inst = form.save(commit=False)
        inst.organizer = request.user
        inst.save()
        public_url = f"{settings.DOMAIN}events/{inst.pk}/invite/{uuid.uuid4()}"
        inst.public_invite_url = public_url
        inst.save()
        return redirect(reverse("events:events-list"))
    context = {
        "form": form
    }

    return render(request, template_name, context=context)


def events_list_view(request):
    template_name = "events/events_list.html"
    queryset = Event.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


def event_detail_view(request, pk):
    template_name = "events/event_detail.html"
    event = get_object_or_404(Event, pk=pk)
    context = {
        "event": event
    }
    return render(request, template_name, context)


def food_create_view(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse("events:event-create"))

    context = {
        "form": form
    }

    return render(request, "events/food_create.html", context=context)


def drinks_create_view(request):
    form = DrinksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse("events:event-create"))

    context = {
        "form": form
    }
    return render(request, "events/drink_create.html", context=context)


def accept_invite_view(request, pk, invite_pk):
    template_name = "events/accept_invite.html"
    post_data = request.POST
    event = get_object_or_404(Event, pk=pk)
    form = AcceptInvitationForm(request.POST or None, instance=event)
    if form.is_valid():
        inst = form.save(commit=False)
        inst.no_participants += int(request.POST["no_participants"])
        inst.save()
        attendee = Attendee.objects.create(name=post_data["attendee_name"],
                                food=Food.objects.get(pk=post_data["food"]),
                                drinks=Drink.objects.get(pk=post_data["drinks"]))
        attendee.event.add(event)
        return redirect(reverse("events:event-detail", kwargs={"pk": pk}))
    context = {
        "form": form,
    }
    return render(request, template_name, context=context)
