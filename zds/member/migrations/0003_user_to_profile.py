# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def user_to_profile(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Ban = apps.get_model("member", "Ban")
    for ban in Ban.objects.all().select_related('user', 'moderator'):
        ban.profile = ban.user.profile
        ban.tmp_moderator = ban.moderator.profile
        ban.save()

    KarmaNote = apps.get_model("member", "KarmaNote")
    for karma_note in KarmaNote.objects.all().select_related('user', 'staff'):
        karma_note.profile = karma_note.user.profile
        karma_note.tmp_staff = karma_note.staff.profile
        karma_note.save()

    TokenForgotPassword = apps.get_model("member", "TokenForgotPassword")
    for token_forgot_password in TokenForgotPassword.objects.all().select_related('user'):
        token_forgot_password.profile = token_forgot_password.user.profile
        token_forgot_password.save()

    TokenRegister = apps.get_model("member", "TokenRegister")
    for token_register in TokenRegister.objects.all().select_related('user'):
        token_register.profile = token_register.user.profile
        token_register.save()



class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20150516_2219'),
    ]

    operations = [
        migrations.RunPython(user_to_profile),
    ]
