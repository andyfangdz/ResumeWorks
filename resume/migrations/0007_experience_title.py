# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_personal_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
