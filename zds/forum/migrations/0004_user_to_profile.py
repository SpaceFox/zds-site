# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def user_to_profile(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Topic = apps.get_model("forum", "Topic")
    for topic in Topic.objects.all().select_related('author'):
        topic.tmp_author = topic.author.profile
        topic.save()

    TopicFollowed = apps.get_model("forum", "TopicFollowed")
    for topic_followed in TopicFollowed.objects.all().select_related('user'):
        topic_followed.profile = topic_followed.user.profile
        topic_followed.save()

    TopicRead = apps.get_model("forum", "TopicRead")
    for topic_read in TopicRead.objects.all().select_related('user'):
        topic_read.profile = topic_read.user.profile
        topic_read.save()


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20150516_2200'),
    ]

    operations = [
        migrations.RunPython(user_to_profile),
    ]
