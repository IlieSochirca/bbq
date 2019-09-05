# Create your models here.
from django.db import models

food_choices = (
    ("pork", "PORK"),
    ("kitchen", "KITCHEN"),
    ("beef", "BEEF")
)


class Food(models.Model):
    """
    Food Model Declaration
    """
    name = models.CharField(max_length=50, help_text="Food Name")
    quantity = models.IntegerField(help_text="Food Quantity")

    def __str__(self):
        return self.name


class Drink(models.Model):
    """
    Drink Model Declaration
    """
    name = models.CharField(max_length=50, help_text="Drink Name")
    quantity = models.IntegerField(help_text="Drink Quantity")

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Event Model Declaration
    """
    name = models.CharField(max_length=100)
    day = models.DateField("Event Day", help_text="Day of the event")
    start_time = models.TimeField("Event Starting time", help_text="Starting time")
    end_time = models.TimeField("Event Final time", help_text="Final time")
    description = models.TextField("Event Description", help_text="Event details", blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="Food")
    drinks = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="Drink")
    public_invite_url = models.URLField(max_length=200, null=True)
    no_participants = models.IntegerField(null=True, help_text="Number of Participants")

    def __str__(self):
        return self.name
