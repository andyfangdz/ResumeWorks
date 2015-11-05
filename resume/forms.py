from django import forms
from .models import Project, Experience, Education, Skill, SkillGroup, Course, Reference, Personal, ReferenceRequest, Award


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date_started', 'date_ended', 'description', 'url', 'is_current']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'date_started', 'date_ended', 'is_current', 'description', 'projects']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'Major', 'Description', 'GPA', 'GPA_major', 'show_gpa', 'show_gpa_major', 'date_started', 'date_ended']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'belong_to']


class SkillGroupForm(forms.ModelForm):
    class Meta:
        model = SkillGroup
        fields = ['name']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'major']


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['name', 'title', 'description']


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['name', 'phone', 'location']


class ReferenceRequestForm(forms.ModelForm):
    class Meta:
        model = ReferenceRequest
        fields = ['name', 'email', 'references']


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['name', 'date_awerded', 'awerder', 'projects']


