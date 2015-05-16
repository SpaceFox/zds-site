# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20150516_2219'),
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tmp_authors',
            field=models.ManyToManyField(to='member.Profile', verbose_name=b'Auteurs', db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tutorialread',
            name='profile',
            field=models.ForeignKey(related_name='tuto_notes_read', default=1, to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='validation',
            name='tmp_validator',
            field=models.ForeignKey(related_name='author_validations', verbose_name=b'Validateur', blank=True, to='member.Profile', null=True),
            preserve_default=True,
        ),
    ]
