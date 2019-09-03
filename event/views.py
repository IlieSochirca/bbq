from django.shortcuts import render

from .forms import EventForm
from .models import Event


# Create your views here.


def event_create_view(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }

    return render(request, "events/event_create.html", context=context )



# def event_detail_view(request):

