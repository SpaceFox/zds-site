# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def user_to_profile(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Tutorial = apps.get_model("tutorial", "Tutorial")
    for tutorial in Tutorial.objects.all().select_related('author'):
        for author in tutorial.authors.all():
            tutorial.tmp_authors.add(author.profile)
        tutorial.save()

    TutorialRead = apps.get_model("tutorial", "TutorialRead")
    for tutorial_read in TutorialRead.objects.all().select_related('user'):
        tutorial_read.profile = tutorial_read.user.profile
        tutorial_read.save()

    Validation = apps.get_model("tutorial", "Validation")
    for validation in Validation.objects.all().select_related('validator'):
        if validation.validator:
            validation.tmp_validator = validation.validator.profile
            validation.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_auto_20150516_2311'),
    ]

    operations = [
        migrations.RunPython(user_to_profile),
    ]
