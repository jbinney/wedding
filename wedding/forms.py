from wedding.models import RSVP

from django.forms import ModelForm


class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'email', 'attending', 'main_course', 'is_vegetarian',
                  'has_significant_other', 'significant_other_name']
        error_messages = {
            'name': {
                'required': "This is required."
            },
            'email': {
                'required': "This is required."
            }
        }

    def clean(self):
        cleaned_data = super(RSVPForm, self).clean()
        self.validate_dependent_field(
            'attending',
            'main_course',
            "You must choose one of these options."
        )
        self.validate_dependent_field(
            'has_significant_other',
            'significant_other_name',
            "We need to know his/her name to seat you together."
        )
        return cleaned_data

    def validate_dependent_field(
            self,
            boolean_field,
            required_field,
            error_message):
        boolean_value = self.cleaned_data.get(boolean_field)
        required_value = self.cleaned_data.get(required_field)
        if boolean_value and not required_value:
            self.add_error(required_field, error_message)
