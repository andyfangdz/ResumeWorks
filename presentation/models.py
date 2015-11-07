from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import CharField
from django_extensions.db.fields import AutoSlugField
from django.db.models import DateTimeField
from django.db.models import ManyToManyField
from django.db.models import ForeignKey
from django.db.models import BooleanField

# Create your models here.

class Presentation(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', null=True, blank=True)
    is_default = BooleanField()
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    projects = ManyToManyField('resume.Project', null=True, blank=True)
    educations = ManyToManyField('resume.Education', null=True, blank=True)
    experiences = ManyToManyField('resume.Experience', null=True, blank=True)
    courses = ManyToManyField('resume.Course', null=True, blank=True)
    personal = ForeignKey('resume.Personal', null=True, blank=True)
    skill_groups = ManyToManyField('resume.SkillGroup', null=True, blank=True)
    skills = ManyToManyField('resume.Skill', null=True, blank=True)
    references = ManyToManyField('resume.Reference', null=True, blank=True)
    awards = ManyToManyField('resume.Award', null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('presentation_presentation_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('ResumeWorks_presentation_update', args=(self.slug,))