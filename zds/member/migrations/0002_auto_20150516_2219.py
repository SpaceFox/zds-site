# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ban',
            name='profile',
            field=models.ForeignKey(default=1, verbose_name=b'Sanctionn\xc3\xa9', to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ban',
            name='tmp_moderator',
            field=models.ForeignKey(related_name='bans', default=1, verbose_name=b'Moderateur', to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='karmanote',
            name='profile',
            field=models.ForeignKey(related_name='karmanote_user', default=1, to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='karmanote',
            name='tmp_staff',
            field=models.ForeignKey(related_name='karmanote_staff', default=1, to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tokenforgotpassword',
            name='profile',
            field=models.ForeignKey(default=1, verbose_name=b'Utilisateur', to='member.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tokenregister',
            name='profile',
            field=models.ForeignKey(default=1, verbose_name=b'Utilisateur', to='member.Profile'),
            preserve_default=False,
        ),
    ]
