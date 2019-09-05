from django import forms
from django.conf import settings
from django.forms import widgets
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Event, Food


class RelatedFieldWidgetCanAdd(widgets.Select):

    def __init__(self, related_model, related_url=None, *args, **kw):
        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = ''

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        print("acolo", output)
        print("aici", self.related_url)
        output.append('<a href="{%s}"> ' % (self.related_url))
        output.append('<img src="%sadmin/img/icon_addlink.gif" width="10" height="10" alt="%s"/></a>' % (
            settings.STATIC_URL, 'Add Another'))
        return mark_safe(''.join(output))


class EventForm(forms.ModelForm):
    """
    Event Form
    """

    food = forms.ModelChoiceField(required=False,
                                  queryset=Food.objects.all(),
                                  widget=RelatedFieldWidgetCanAdd(Food, related_url="events:food-add"))

    class Meta:
        model = Event
        fields = [
            "name", "day", "start_time", "end_time", "description", "food", "drinks", "no_participants"
        ]


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name", "quantity"]
