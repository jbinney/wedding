# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('attending', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('main_course', models.CharField(blank=True, max_length=16, choices=[(b'filet', b'Pepper Trio Seared Filet Mignon'), (b'duck', b'Sugar and Sherry Glazed Maple Leaf Muscovy Duck'), (b'bass', b'Seared Chilean Sea Bass'), (b'gnocchi', b'Pan Seared Gnocchi')])),
                ('has_significant_other', models.BooleanField(default=False)),
                ('significant_other_name', models.CharField(max_length=128, blank=True)),
            ],
        ),
    ]
