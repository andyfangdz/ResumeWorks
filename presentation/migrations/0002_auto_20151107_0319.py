# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='awards',
            field=models.ManyToManyField(to='resume.Award', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='courses',
            field=models.ManyToManyField(to='resume.Course', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='educations',
            field=models.ManyToManyField(to='resume.Education', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='experiences',
            field=models.ManyToManyField(to='resume.Experience', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='personal',
            field=models.ForeignKey(blank=True, to='resume.Personal', null=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='projects',
            field=models.ManyToManyField(to='resume.Project', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='references',
            field=models.ManyToManyField(to='resume.Reference', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='skill_groups',
            field=models.ManyToManyField(to='resume.SkillGroup', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='skills',
            field=models.ManyToManyField(to='resume.Skill', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'name', null=True, editable=False, blank=True),
        ),
    ]
