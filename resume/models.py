from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import CharField
from django_extensions.db.fields import AutoSlugField
from django.db.models import DateTimeField
from django.db.models import DateField
from django.db.models import TextField
from django.db.models import BooleanField
from django.db.models import ManyToManyField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import EmailField
from django.db.models import IntegerField


class Project(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    date_started = DateField()
    date_ended = DateField(null=True, blank=True)
    description = TextField(blank=True, null=True)
    url = CharField(max_length=255, null=True, blank=True)
    is_current = BooleanField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_project_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_project_update', args=(self.slug,))


class Experience(models.Model):

    # Fields
    company = CharField(max_length=255)
    slug = AutoSlugField(populate_from='company', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    date_started = DateField()
    date_ended = DateField(blank=True, null=True)
    is_current = BooleanField()
    description = TextField(blank=True, null=True)

    # Relationship Fields
    projects = ManyToManyField('resume.Project', null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_experience_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_experience_update', args=(self.slug,))


class Education(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    Major = CharField(max_length=30)
    Description = TextField(blank=True, null=True)
    GPA = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    GPA_major = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    show_gpa = BooleanField()
    show_gpa_major = BooleanField()
    date_started = DateField()
    date_ended = DateField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_education_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_education_update', args=(self.slug,))


class Skill(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    years = IntegerField(null=True, blank=True)
    proficiency = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    level = CharField(max_length=255, blank=True, null=True)

    # Relationship Fields
    belong_to = ForeignKey('resume.SkillGroup',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_skill_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_skill_update', args=(self.slug,))


class SkillGroup(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_skillgroup_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_skillgroup_update', args=(self.slug,))


class Course(models.Model):

    # Fields
    name = CharField(max_length=255)
    number = CharField(max_length=255)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    major = CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.number

    def get_absolute_url(self):
        return reverse('resume_course_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_course_update', args=(self.slug,))


class Reference(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    title = CharField(max_length=300)
    description = TextField(null=True, blank=True)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_reference_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_reference_update', args=(self.slug,))


class Personal(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    phone = CharField(max_length=30, null=True, blank=True)
    location = CharField(max_length=30, null=True, blank=True)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_personal_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_personal_update', args=(self.slug,))


class ReferenceRequest(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    email = EmailField(max_length=255)

    # Relationship Fields
    references = ManyToManyField('resume.Reference',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_referencerequest_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_referencerequest_update', args=(self.slug,))


class Award(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    date_awerded = DateField()
    awerder = CharField(max_length=255, null=True, blank=True)

    # Relationship Fields
    projects = ManyToManyField('resume.Project', null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('resume_award_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('resume_award_update', args=(self.slug,))
