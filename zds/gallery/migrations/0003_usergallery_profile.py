# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('gallery', '0002_auto_20150409_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergallery',
            name='profile',
            field=models.ForeignKey(default=1, verbose_name='Membre', to='member.Profile'),
            preserve_default=False,
        ),
    ]
