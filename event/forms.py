from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    Event Form
    """

    class Meta:
        model = Event
        fields = [
            "name", "day", "start_time", "end_time", "description", "meat"
        ]
