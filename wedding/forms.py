from wedding.models import RSVP

from django.forms import ModelForm


class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'email', 'attending', 'main_course', 'is_vegetarian',
                  'has_significant_other', 'significant_other_name']
