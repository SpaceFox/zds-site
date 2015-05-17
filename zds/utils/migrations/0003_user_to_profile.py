# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def user_to_profile(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Alert = apps.get_model("utils", "Alert")
    for alert in Alert.objects.all().select_related('author'):
        alert.tmp_author = alert.author.profile
        alert.save()

    Comment = apps.get_model("utils", "Comment")
    for comment in Comment.objects.all().select_related('author', 'editor'):
        comment.tmp_author = comment.author.profile
        if comment.editor:
            comment.tmp_editor = comment.editor.profile
        comment.save()

    CommentLike = apps.get_model("utils", "CommentLike")
    for comment_like in CommentLike.objects.all().select_related('user'):
        comment_like.profile = comment_like.user.profile
        comment_like.save()

    CommentDislike = apps.get_model("utils", "CommentDislike")
    for comment_dislike in CommentDislike.objects.all().select_related('user'):
        comment_dislike.profile = comment_dislike.user.profile
        comment_dislike.save()


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_auto_20150516_2314'),
    ]

    operations = [
        migrations.RunPython(user_to_profile),
    ]
