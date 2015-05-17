# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def user_to_profile(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    UserGallery = apps.get_model("gallery", "UserGallery")
    for user_gallery in UserGallery.objects.all().select_related('user'):
        user_gallery.profile = user_gallery.user.profile
        user_gallery.save()


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_usergallery_profile'),
    ]

    operations = [
        migrations.RunPython(user_to_profile),
    ]
