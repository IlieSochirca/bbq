from django import forms
from django.forms import widgets
from django.urls import reverse
from django.utils.safestring import mark_safe

from bbq import settings
from .models import Event, Food, Drink, Attendee


class RelatedFieldWidgetCanAdd(widgets.Select):

    def __init__(self, related_model, related_url=None, *args, **kw):
        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = f'admin:{info}_{info}_add'
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        url = f'<a href="{self.related_url}?_to_field=id&_popup=1" class="add-another" id="add_id_{name}" onclick="return showAddAnotherPopup(this);"> '
        output.append(url)
        output.append(
            f'<img src="{settings.STATIC_URL}admin/img/icon_addlink.gif" width="10" height="10" alt="Add Another"/></a>')
        return mark_safe(''.join(output))


class EventForm(forms.ModelForm):
    """
    Event Form
    """

    food = forms.ModelChoiceField(queryset=Food.objects.all(),
                                  required=False,
                                  widget=RelatedFieldWidgetCanAdd(Food, related_url="events:food-add"))

    drinks = forms.ModelChoiceField(queryset=Drink.objects.all(),
                                    required=False,
                                    widget=RelatedFieldWidgetCanAdd(Drink, related_url="events:drinks-add"))

    class Meta:
        model = Event
        fields = [
            "name", "day", "start_time", "end_time", "description", "food", "drinks"
        ]


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name", "quantity"]


class DrinksForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ["name", "quantity"]


class AcceptInvitationForm(forms.ModelForm):
    no_guests = forms.IntegerField(required=False)

    class Meta:
        model = Attendee
        fields = ["name", "food", "desired_food_quantity", "drinks", "desired_drinks_quantity", "no_guests"]

    def __init__(self, event, *args, **kwargs):
        super(AcceptInvitationForm, self).__init__(*args, **kwargs)
        event = Event.objects.get(pk=event.pk)
        self.fields["food"].queryset = Food.objects.filter(EventFood=event)
        self.fields["drinks"].queryset = Drink.objects.filter(EventDrink=event)
