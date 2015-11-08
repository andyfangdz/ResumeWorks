from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from .models import Project, Experience, Education, Skill, SkillGroup, Course, Reference, Personal, ReferenceRequest, Award


class ProjectAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'date_started', 'date_ended', 'description', 'url', 'is_current']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'date_started', 'date_ended', 'description', 'url', 'is_current']

admin.site.register(Project, ProjectAdmin)


class ExperienceAdmin(SummernoteModelAdmin):
    list_display = ['company', 'slug', 'created', 'last_updated', 'date_started', 'date_ended', 'is_current', 'description']
    # readonly_fields = ['company', 'slug', 'created', 'last_updated', 'date_started', 'date_ended', 'is_current', 'description']

admin.site.register(Experience, ExperienceAdmin)


class EducationAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'Major', 'Description', 'GPA', 'GPA_major', 'show_gpa', 'show_gpa_major', 'date_started', 'date_ended']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'Major', 'Description', 'GPA', 'GPA_major', 'show_gpa', 'show_gpa_major', 'date_started', 'date_ended']

admin.site.register(Education, EducationAdmin)


class SkillAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Skill, SkillAdmin)


class SkillGroupAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(SkillGroup, SkillGroupAdmin)


class CourseAdmin(SummernoteModelAdmin):
    list_display = ['name', 'number', 'created', 'last_updated', 'major']
    # readonly_fields = ['name', 'number', 'created', 'last_updated', 'major']

admin.site.register(Course, CourseAdmin)


class ReferenceAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'title', 'description']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'title', 'description']

admin.site.register(Reference, ReferenceAdmin)


class PersonalAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'phone', 'location']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'phone', 'location']

admin.site.register(Personal, PersonalAdmin)


class ReferenceRequestAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'email']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'email']

admin.site.register(ReferenceRequest, ReferenceRequestAdmin)


class AwardAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'date_awerded', 'awerder']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'date_awerded', 'awerder']

admin.site.register(Award, AwardAdmin)
