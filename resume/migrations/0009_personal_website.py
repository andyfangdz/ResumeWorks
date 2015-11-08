# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_personal_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='website',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
