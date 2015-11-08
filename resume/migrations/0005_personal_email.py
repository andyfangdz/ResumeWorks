# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20151107_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
