import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Project, Experience, Education, Skill, SkillGroup, Course, Reference, Personal, ReferenceRequest, Award


def create_project(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["date_started"] = "date_started"
    defaults["date_ended"] = "date_ended"
    defaults["description"] = "description"
    defaults["url"] = "url"
    defaults["is_current"] = "is_current"
    defaults.update(**kwargs)
    return Project.objects.create(**defaults)


def create_experience(**kwargs):
    defaults = {}
    defaults["company"] = "company"
    defaults["slug"] = "slug"
    defaults["date_started"] = "date_started"
    defaults["date_ended"] = "date_ended"
    defaults["is_current"] = "is_current"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    if "projects" not in defaults:
        defaults["projects"] = create_project()
    return Experience.objects.create(**defaults)


def create_education(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["Major"] = "Major"
    defaults["Description"] = "Description"
    defaults["GPA"] = "GPA"
    defaults["GPA_major"] = "GPA_major"
    defaults["show_gpa"] = "show_gpa"
    defaults["show_gpa_major"] = "show_gpa_major"
    defaults["date_started"] = "date_started"
    defaults["date_ended"] = "date_ended"
    defaults.update(**kwargs)
    return Education.objects.create(**defaults)


def create_skill(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    if "belong_to" not in defaults:
        defaults["belong_to"] = create_skillgroup()
    return Skill.objects.create(**defaults)


def create_skillgroup(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    return SkillGroup.objects.create(**defaults)


def create_course(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["major"] = "major"
    defaults.update(**kwargs)
    return Course.objects.create(**defaults)


def create_reference(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["title"] = "title"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    return Reference.objects.create(**defaults)


def create_personal(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["phone"] = "phone"
    defaults["location"] = "location"
    defaults.update(**kwargs)
    return Personal.objects.create(**defaults)


def create_referencerequest(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["email"] = "email"
    defaults.update(**kwargs)
    if "references" not in defaults:
        defaults["references"] = create_reference()
    return ReferenceRequest.objects.create(**defaults)


def create_award(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["date_awerded"] = "date_awerded"
    defaults["awerder"] = "awerder"
    defaults.update(**kwargs)
    if "projects" not in defaults:
        defaults["projects"] = create_project()
    return Award.objects.create(**defaults)


class ProjectViewTest(unittest.TestCase):
    '''
    Tests for Project
    '''
    def setUp(self):
        self.client = Client()

    def test_list_project(self):
        url = reverse('ResumeWorks_project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_project(self):
        url = reverse('ResumeWorks_project_create')
        data = {
            "name": "name",
            "slug": "slug",
            "date_started": "date_started",
            "date_ended": "date_ended",
            "description": "description",
            "url": "url",
            "is_current": "is_current",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_project(self):
        project = create_project()
        url = reverse('ResumeWorks_project_detail', args=[project.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_project(self):
        project = create_project()
        data = {
            "name": "name",
            "slug": "slug",
            "date_started": "date_started",
            "date_ended": "date_ended",
            "description": "description",
            "url": "url",
            "is_current": "is_current",
        }
        url = reverse('ResumeWorks_project_update', args=[project.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ExperienceViewTest(unittest.TestCase):
    '''
    Tests for Experience
    '''
    def setUp(self):
        self.client = Client()

    def test_list_experience(self):
        url = reverse('ResumeWorks_experience_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_experience(self):
        url = reverse('ResumeWorks_experience_create')
        data = {
            "company": "company",
            "slug": "slug",
            "date_started": "date_started",
            "date_ended": "date_ended",
            "is_current": "is_current",
            "description": "description",
            "projects": create_project().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_experience(self):
        experience = create_experience()
        url = reverse('ResumeWorks_experience_detail', args=[experience.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_experience(self):
        experience = create_experience()
        data = {
            "company": "company",
            "slug": "slug",
            "date_started": "date_started",
            "date_ended": "date_ended",
            "is_current": "is_current",
            "description": "description",
            "projects": create_project().id,
        }
        url = reverse('ResumeWorks_experience_update', args=[experience.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EducationViewTest(unittest.TestCase):
    '''
    Tests for Education
    '''
    def setUp(self):
        self.client = Client()

    def test_list_education(self):
        url = reverse('ResumeWorks_education_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_education(self):
        url = reverse('ResumeWorks_education_create')
        data = {
            "name": "name",
            "slug": "slug",
            "Major": "Major",
            "Description": "Description",
            "GPA": "GPA",
            "GPA_major": "GPA_major",
            "show_gpa": "show_gpa",
            "show_gpa_major": "show_gpa_major",
            "date_started": "date_started",
            "date_ended": "date_ended",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_education(self):
        education = create_education()
        url = reverse('ResumeWorks_education_detail', args=[education.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_education(self):
        education = create_education()
        data = {
            "name": "name",
            "slug": "slug",
            "Major": "Major",
            "Description": "Description",
            "GPA": "GPA",
            "GPA_major": "GPA_major",
            "show_gpa": "show_gpa",
            "show_gpa_major": "show_gpa_major",
            "date_started": "date_started",
            "date_ended": "date_ended",
        }
        url = reverse('ResumeWorks_education_update', args=[education.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SkillViewTest(unittest.TestCase):
    '''
    Tests for Skill
    '''
    def setUp(self):
        self.client = Client()

    def test_list_skill(self):
        url = reverse('ResumeWorks_skill_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_skill(self):
        url = reverse('ResumeWorks_skill_create')
        data = {
            "name": "name",
            "slug": "slug",
            "belong_to": create_skillgroup().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_skill(self):
        skill = create_skill()
        url = reverse('ResumeWorks_skill_detail', args=[skill.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_skill(self):
        skill = create_skill()
        data = {
            "name": "name",
            "slug": "slug",
            "belong_to": create_skillgroup().id,
        }
        url = reverse('ResumeWorks_skill_update', args=[skill.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SkillGroupViewTest(unittest.TestCase):
    '''
    Tests for SkillGroup
    '''
    def setUp(self):
        self.client = Client()

    def test_list_skillgroup(self):
        url = reverse('ResumeWorks_skillgroup_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_skillgroup(self):
        url = reverse('ResumeWorks_skillgroup_create')
        data = {
            "name": "name",
            "slug": "slug",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_skillgroup(self):
        skillgroup = create_skillgroup()
        url = reverse('ResumeWorks_skillgroup_detail', args=[skillgroup.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_skillgroup(self):
        skillgroup = create_skillgroup()
        data = {
            "name": "name",
            "slug": "slug",
        }
        url = reverse('ResumeWorks_skillgroup_update', args=[skillgroup.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CourseViewTest(unittest.TestCase):
    '''
    Tests for Course
    '''
    def setUp(self):
        self.client = Client()

    def test_list_course(self):
        url = reverse('ResumeWorks_course_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_course(self):
        url = reverse('ResumeWorks_course_create')
        data = {
            "name": "name",
            "slug": "slug",
            "major": "major",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_course(self):
        course = create_course()
        url = reverse('ResumeWorks_course_detail', args=[course.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_course(self):
        course = create_course()
        data = {
            "name": "name",
            "slug": "slug",
            "major": "major",
        }
        url = reverse('ResumeWorks_course_update', args=[course.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReferenceViewTest(unittest.TestCase):
    '''
    Tests for Reference
    '''
    def setUp(self):
        self.client = Client()

    def test_list_reference(self):
        url = reverse('ResumeWorks_reference_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_reference(self):
        url = reverse('ResumeWorks_reference_create')
        data = {
            "name": "name",
            "slug": "slug",
            "title": "title",
            "description": "description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_reference(self):
        reference = create_reference()
        url = reverse('ResumeWorks_reference_detail', args=[reference.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_reference(self):
        reference = create_reference()
        data = {
            "name": "name",
            "slug": "slug",
            "title": "title",
            "description": "description",
        }
        url = reverse('ResumeWorks_reference_update', args=[reference.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PersonalViewTest(unittest.TestCase):
    '''
    Tests for Personal
    '''
    def setUp(self):
        self.client = Client()

    def test_list_personal(self):
        url = reverse('ResumeWorks_personal_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_personal(self):
        url = reverse('ResumeWorks_personal_create')
        data = {
            "name": "name",
            "slug": "slug",
            "phone": "phone",
            "location": "location",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_personal(self):
        personal = create_personal()
        url = reverse('ResumeWorks_personal_detail', args=[personal.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_personal(self):
        personal = create_personal()
        data = {
            "name": "name",
            "slug": "slug",
            "phone": "phone",
            "location": "location",
        }
        url = reverse('ResumeWorks_personal_update', args=[personal.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReferenceRequestViewTest(unittest.TestCase):
    '''
    Tests for ReferenceRequest
    '''
    def setUp(self):
        self.client = Client()

    def test_list_referencerequest(self):
        url = reverse('ResumeWorks_referencerequest_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_referencerequest(self):
        url = reverse('ResumeWorks_referencerequest_create')
        data = {
            "name": "name",
            "slug": "slug",
            "email": "email",
            "references": create_reference().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_referencerequest(self):
        referencerequest = create_referencerequest()
        url = reverse('ResumeWorks_referencerequest_detail', args=[referencerequest.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_referencerequest(self):
        referencerequest = create_referencerequest()
        data = {
            "name": "name",
            "slug": "slug",
            "email": "email",
            "references": create_reference().id,
        }
        url = reverse('ResumeWorks_referencerequest_update', args=[referencerequest.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AwardViewTest(unittest.TestCase):
    '''
    Tests for Award
    '''
    def setUp(self):
        self.client = Client()

    def test_list_award(self):
        url = reverse('ResumeWorks_award_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_award(self):
        url = reverse('ResumeWorks_award_create')
        data = {
            "name": "name",
            "slug": "slug",
            "date_awerded": "date_awerded",
            "awerder": "awerder",
            "projects": create_project().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_award(self):
        award = create_award()
        url = reverse('ResumeWorks_award_detail', args=[award.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_award(self):
        award = create_award()
        data = {
            "name": "name",
            "slug": "slug",
            "date_awerded": "date_awerded",
            "awerder": "awerder",
            "projects": create_project().id,
        }
        url = reverse('ResumeWorks_award_update', args=[award.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


