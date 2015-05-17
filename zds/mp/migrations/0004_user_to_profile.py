# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def user_to_profile(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    PrivatePost = apps.get_model("mp", "PrivatePost")
    for private_post in PrivatePost.objects.all().select_related('author'):
        private_post.tmp_author = private_post.author.profile
        private_post.save()

    PrivateTopic = apps.get_model("mp", "PrivateTopic")
    for private_topic in PrivateTopic.objects.all().select_related('author', 'participants'):
        private_topic.tmp_author = private_topic.author.profile
        for participant in private_topic.participants.all():
            private_topic.tmp_participants.add(participant.profile)
        private_topic.save()

    PrivateTopicRead = apps.get_model("mp", "PrivateTopicRead")
    for private_topic_read in PrivateTopicRead.objects.all().select_related('user'):
        private_topic_read.profile = private_topic_read.user.profile
        private_topic_read.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0003_auto_20150516_2310'),
    ]

    operations = [
        migrations.RunPython(user_to_profile),
    ]
