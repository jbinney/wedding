from wedding.forms import RSVPForm
from wedding.models import RSVP

from django.shortcuts import render
from django.views.generic.base import View, TemplateView


def get_rsvp_context(context):
    context['MAIN_COURSE_CHOICES'] = RSVP.MAIN_COURSE_CHOICES
    return context


class RSVPView(TemplateView):
    template_name='wedding/rsvp.html'

    def get_context_data(self, **kwargs):
        context = super(RSVPView, self).get_context_data(**kwargs)
        return get_rsvp_context(context)


class SubmitRSVPView(View):
    def post(self, request):
        form = RSVPForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                'wedding/rsvp.html',
                get_rsvp_context({
                    'data': form.cleaned_data,
                    'errors': form.errors
                })
            )
        else:
            form.save()
            return render(
                request,
                'wedding/rsvp_confirmation.html',
                {'data': form.cleaned_data}
            )
