# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('forum', '0002_auto_20150410_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='tmp_author',
            field=models.ForeignKey(related_name='topics', default=1, verbose_name=b'Auteur', to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topicfollowed',
            name='profile',
            field=models.ForeignKey(related_name='topics_followed', default=1, to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topicread',
            name='profile',
            field=models.ForeignKey(related_name='topics_read', default=1, to='member.Profile'),
            preserve_default=False,
        ),
    ]
