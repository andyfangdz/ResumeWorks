# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_experience_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
