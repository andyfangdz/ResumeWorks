# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='projects',
            field=models.ManyToManyField(to='resume.Project', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'company', editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='location',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='phone',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
