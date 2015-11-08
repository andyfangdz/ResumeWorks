# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_award_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
