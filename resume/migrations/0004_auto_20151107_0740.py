# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20151107_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='github',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='linkedin',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
