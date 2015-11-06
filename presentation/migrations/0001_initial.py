# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'name', editable=False, blank=True)),
                ('is_default', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('awards', models.ManyToManyField(to='resume.Award')),
                ('courses', models.ManyToManyField(to='resume.Course')),
                ('educations', models.ManyToManyField(to='resume.Education')),
                ('experiences', models.ManyToManyField(to='resume.Experience')),
                ('personal', models.ForeignKey(to='resume.Personal')),
                ('projects', models.ManyToManyField(to='resume.Project')),
                ('references', models.ManyToManyField(to='resume.Reference')),
                ('skill_groups', models.ManyToManyField(to='resume.SkillGroup')),
                ('skills', models.ManyToManyField(to='resume.Skill')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
