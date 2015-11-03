from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Project, Experience, Education, Skill, SkillGroup, Course, Reference, Personal, ReferenceRequest, Award
from .forms import ProjectForm, ExperienceForm, EducationForm, SkillForm, SkillGroupForm, CourseForm, ReferenceForm, PersonalForm, ReferenceRequestForm, AwardForm


class ProjectListView(ListView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm


class ExperienceListView(ListView):
    model = Experience


class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm


class ExperienceDetailView(DetailView):
    model = Experience


class ExperienceUpdateView(UpdateView):
    model = Experience
    form_class = ExperienceForm


class EducationListView(ListView):
    model = Education


class EducationCreateView(CreateView):
    model = Education
    form_class = EducationForm


class EducationDetailView(DetailView):
    model = Education


class EducationUpdateView(UpdateView):
    model = Education
    form_class = EducationForm


class SkillListView(ListView):
    model = Skill


class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm


class SkillDetailView(DetailView):
    model = Skill


class SkillUpdateView(UpdateView):
    model = Skill
    form_class = SkillForm


class SkillGroupListView(ListView):
    model = SkillGroup


class SkillGroupCreateView(CreateView):
    model = SkillGroup
    form_class = SkillGroupForm


class SkillGroupDetailView(DetailView):
    model = SkillGroup


class SkillGroupUpdateView(UpdateView):
    model = SkillGroup
    form_class = SkillGroupForm


class CourseListView(ListView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm


class CourseDetailView(DetailView):
    model = Course


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm


class ReferenceListView(ListView):
    model = Reference


class ReferenceCreateView(CreateView):
    model = Reference
    form_class = ReferenceForm


class ReferenceDetailView(DetailView):
    model = Reference


class ReferenceUpdateView(UpdateView):
    model = Reference
    form_class = ReferenceForm


class PersonalListView(ListView):
    model = Personal


class PersonalCreateView(CreateView):
    model = Personal
    form_class = PersonalForm


class PersonalDetailView(DetailView):
    model = Personal


class PersonalUpdateView(UpdateView):
    model = Personal
    form_class = PersonalForm


class ReferenceRequestListView(ListView):
    model = ReferenceRequest


class ReferenceRequestCreateView(CreateView):
    model = ReferenceRequest
    form_class = ReferenceRequestForm


class ReferenceRequestDetailView(DetailView):
    model = ReferenceRequest


class ReferenceRequestUpdateView(UpdateView):
    model = ReferenceRequest
    form_class = ReferenceRequestForm


class AwardListView(ListView):
    model = Award


class AwardCreateView(CreateView):
    model = Award
    form_class = AwardForm


class AwardDetailView(DetailView):
    model = Award


class AwardUpdateView(UpdateView):
    model = Award
    form_class = AwardForm

