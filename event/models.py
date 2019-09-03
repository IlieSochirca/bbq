# Create your models here.
from django.db import models

meat_choices = (
    ("pork", "PORK"),
    ("kitchen","KITCHEN"),
    ("beef", "BEEF")
)


class Event(models.Model):
    """
    Event Model
    """
    name = models.CharField(max_length=100)
    day = models.DateField("Event Day", help_text="Day of the event")
    start_time = models.TimeField("Event Starting time", help_text="Starting time")
    end_time = models.TimeField("Event Final time", help_text="Final time")
    description = models.TextField("Event Description", help_text="Event details", blank=True, null=True)
    meat = models.CharField(max_length=50, help_text="Meat for Bbq", choices=meat_choices)

    def __str__(self):
        return self.name
