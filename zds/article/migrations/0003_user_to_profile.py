# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def user_to_profile(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Article = apps.get_model("article", "Article")
    for article in Article.objects.all().select_related('author'):
        for author in article.authors.all():
            article.tmp_authors.add(author.profile)
        article.save()

    ArticleRead = apps.get_model("article", "ArticleRead")
    for article_read in ArticleRead.objects.all().select_related('user'):
        article_read.profile = article_read.user.profile
        article_read.save()

    Validation = apps.get_model("article", "Validation")
    for validation in Validation.objects.all().select_related('validator'):
        if validation.validator:
            validation.tmp_validator = validation.validator.profile
            validation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150516_2153'),
    ]

    operations = [
        migrations.RunPython(user_to_profile),
    ]
