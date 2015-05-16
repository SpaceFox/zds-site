# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20150516_2219'),
        ('mp', '0002_auto_20150416_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatepost',
            name='tmp_author',
            field=models.ForeignKey(related_name='privateposts', default=1, verbose_name=b'Auteur', to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privatetopic',
            name='tmp_author',
            field=models.ForeignKey(related_name='author', default=1, verbose_name='Auteur', to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privatetopic',
            name='tmp_participants',
            field=models.ManyToManyField(related_name='participants', verbose_name='Participants', to='member.Profile', db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='privatetopicread',
            name='profile',
            field=models.ForeignKey(related_name='privatetopics_read', default=1, to='member.Profile'),
            preserve_default=False,
        ),
    ]
