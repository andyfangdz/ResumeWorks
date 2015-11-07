# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20151106_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='proficiency',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='years',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
