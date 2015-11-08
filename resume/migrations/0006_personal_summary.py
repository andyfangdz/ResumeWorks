# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_personal_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='summary',
            field=models.TextField(null=True, blank=True),
        ),
    ]
