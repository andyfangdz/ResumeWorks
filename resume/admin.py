from django.contrib import admin
from django import forms
from .models import Project, Experience, Education, Skill, SkillGroup, Course, Reference, Personal, ReferenceRequest, Award


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'date_started', 'date_ended', 'description', 'url', 'is_current']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'date_started', 'date_ended', 'description', 'url', 'is_current']

admin.site.register(Project, ProjectAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'slug', 'created', 'last_updated', 'date_started', 'date_ended', 'is_current', 'description']
    # readonly_fields = ['company', 'slug', 'created', 'last_updated', 'date_started', 'date_ended', 'is_current', 'description']

admin.site.register(Experience, ExperienceAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'Major', 'Description', 'GPA', 'GPA_major', 'show_gpa', 'show_gpa_major', 'date_started', 'date_ended']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'Major', 'Description', 'GPA', 'GPA_major', 'show_gpa', 'show_gpa_major', 'date_started', 'date_ended']

admin.site.register(Education, EducationAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Skill, SkillAdmin)


class SkillGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(SkillGroup, SkillGroupAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'created', 'last_updated', 'major']
    # readonly_fields = ['name', 'number', 'created', 'last_updated', 'major']

admin.site.register(Course, CourseAdmin)


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'title', 'description']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'title', 'description']

admin.site.register(Reference, ReferenceAdmin)


class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'phone', 'location']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'phone', 'location']

admin.site.register(Personal, PersonalAdmin)


class ReferenceRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'email']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'email']

admin.site.register(ReferenceRequest, ReferenceRequestAdmin)


class AwardAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated', 'date_awerded', 'awerder']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'date_awerded', 'awerder']

admin.site.register(Award, AwardAdmin)
