# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20150516_2219'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='tmp_author',
            field=models.ForeignKey(related_name='alerts', default=1, verbose_name=b'Auteur', to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='tmp_author',
            field=models.ForeignKey(related_name='comments', default=1, verbose_name=b'Auteur', to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='tmp_editor',
            field=models.ForeignKey(related_name='comments-editor', verbose_name=b'Editeur', blank=True, to='member.Profile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentdislike',
            name='profile',
            field=models.ForeignKey(related_name='post_disliked', default=1, to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentlike',
            name='profile',
            field=models.ForeignKey(related_name='post_liked', default=1, to='member.Profile'),
            preserve_default=False,
        ),
    ]
