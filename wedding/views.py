from wedding.models import RSVP

from django.views.generic.base import View, TemplateView


class RSVPView(TemplateView):
    template_name='wedding/rsvp.html'

    def get_context_data(self, **kwargs):
        context = super(RSVPView, self).get_context_data(**kwargs)
        context['MAIN_COURSE_CHOICES'] = RSVP.MAIN_COURSE_CHOICES
        return context
