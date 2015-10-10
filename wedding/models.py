from django.db import models


class RSVP(models.Model):
    MAIN_COURSE_FILET = "filet"
    MAIN_COURSE_DUCK = "duck"
    MAIN_COURSE_BASS = "bass"
    MAIN_COURSE_GNOCCHI = "gnocchi"

    MAIN_COURSE_CHOICES = (
        (MAIN_COURSE_FILET, "Pepper Trio Seared Filet Mignon"),
        (MAIN_COURSE_DUCK, "Sugar and Sherry Glazed Maple Leaf Muscovy Duck"),
        (MAIN_COURSE_BASS, "Seared Chilean Sea Bass"),
        (MAIN_COURSE_GNOCCHI, "Pan Seared Gnocchi"),
    )

    name = models.CharField(max_length=128)
    email = models.EmailField()
    attending = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    main_course = models.CharField(
        choices=MAIN_COURSE_CHOICES,
        max_length=16,
        blank=True
    )
    has_significant_other = models.BooleanField(default=False)
    significant_other_name = models.CharField(max_length=128, blank=True)
