from django import forms
from .models import Project, Experience, Education, Skill, SkillGroup, Course, Reference, Personal, ReferenceRequest, Award


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'slug', 'date_started', 'date_ended', 'description', 'url', 'is_current']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'slug', 'date_started', 'date_ended', 'is_current', 'description', 'project']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'slug', 'Major', 'Description', 'GPA', 'GPA_major', 'show_gpa', 'show_gpa_major', 'date_started', 'date_ended']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'slug', 'skillgroup']


class SkillGroupForm(forms.ModelForm):
    class Meta:
        model = SkillGroup
        fields = ['name', 'slug']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'slug', 'major']


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['name', 'slug', 'title', 'description']


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['name', 'slug', 'phone', 'location']


class ReferenceRequestForm(forms.ModelForm):
    class Meta:
        model = ReferenceRequest
        fields = ['name', 'slug', 'email', 'reference']


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['name', 'slug', 'date_awerded', 'awerder', 'project']


