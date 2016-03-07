from wedding.views import RSVPView, SubmitRSVPView

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name='wedding/home.html'),
        name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gifts/$',
        TemplateView.as_view(template_name='wedding/gifts.html'),
        name='gifts'),
    url(r'^location/$',
        TemplateView.as_view(template_name='wedding/location.html'),
        name='location'),
    url(r'^menu/$',
        TemplateView.as_view(template_name='wedding/menu.html'),
        name='menu'),
    url(r'^rsvp/$',
        RSVPView.as_view(),
        name='rsvp'),
    url(r'^schedule/$',
        TemplateView.as_view(template_name='wedding/schedule.html'),
        name='schedule'),
    url(r'^submit_rsvp/$',
        SubmitRSVPView.as_view(),
        name='submit_rsvp'),
]
