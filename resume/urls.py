from django.conf.urls import patterns, url, include
from .views import ProjectListView, ExperienceListView, EducationListView, SkillListView, SkillGroupListView, CourseListView, ReferenceListView, PersonalListView, ReferenceRequestListView, AwardListView
from .views import ProjectDetailView, ExperienceDetailView, EducationDetailView, SkillDetailView, SkillGroupDetailView, CourseDetailView, ReferenceDetailView, PersonalDetailView, ReferenceRequestDetailView, AwardDetailView
from .views import ProjectCreateView, ExperienceCreateView, EducationCreateView, SkillCreateView, SkillGroupCreateView, CourseCreateView, ReferenceCreateView, PersonalCreateView, ReferenceRequestCreateView, AwardCreateView
from .views import ProjectUpdateView, ExperienceUpdateView, EducationUpdateView, SkillUpdateView, SkillGroupUpdateView, CourseUpdateView, ReferenceUpdateView, PersonalUpdateView, ReferenceRequestUpdateView, AwardUpdateView

urlpatterns = patterns('')

urlpatterns += patterns('',
    # urls for Project
    url(r'^ResumeWorks/project/$', ProjectListView.as_view(), name='ResumeWorks_project_list'),
    url(r'^ResumeWorks/project/create/$', ProjectCreateView.as_view(), name='ResumeWorks_project_create'),
    url(r'^ResumeWorks/project/detail/(?P<slug>\S+)/$', ProjectDetailView.as_view(), name='ResumeWorks_project_detail'),
    url(r'^ResumeWorks/project/update/(?P<slug>\S+)/$', ProjectUpdateView.as_view(), name='ResumeWorks_project_update'),
)

urlpatterns += patterns('',
    # urls for Experience
    url(r'^ResumeWorks/experience/$', ExperienceListView.as_view(), name='ResumeWorks_experience_list'),
    url(r'^ResumeWorks/experience/create/$', ExperienceCreateView.as_view(), name='ResumeWorks_experience_create'),
    url(r'^ResumeWorks/experience/detail/(?P<slug>\S+)/$', ExperienceDetailView.as_view(), name='ResumeWorks_experience_detail'),
    url(r'^ResumeWorks/experience/update/(?P<slug>\S+)/$', ExperienceUpdateView.as_view(), name='ResumeWorks_experience_update'),
)

urlpatterns += patterns('',
    # urls for Education
    url(r'^ResumeWorks/education/$', EducationListView.as_view(), name='ResumeWorks_education_list'),
    url(r'^ResumeWorks/education/create/$', EducationCreateView.as_view(), name='ResumeWorks_education_create'),
    url(r'^ResumeWorks/education/detail/(?P<slug>\S+)/$', EducationDetailView.as_view(), name='ResumeWorks_education_detail'),
    url(r'^ResumeWorks/education/update/(?P<slug>\S+)/$', EducationUpdateView.as_view(), name='ResumeWorks_education_update'),
)

urlpatterns += patterns('',
    # urls for Skill
    url(r'^ResumeWorks/skill/$', SkillListView.as_view(), name='ResumeWorks_skill_list'),
    url(r'^ResumeWorks/skill/create/$', SkillCreateView.as_view(), name='ResumeWorks_skill_create'),
    url(r'^ResumeWorks/skill/detail/(?P<slug>\S+)/$', SkillDetailView.as_view(), name='ResumeWorks_skill_detail'),
    url(r'^ResumeWorks/skill/update/(?P<slug>\S+)/$', SkillUpdateView.as_view(), name='ResumeWorks_skill_update'),
)

urlpatterns += patterns('',
    # urls for SkillGroup
    url(r'^ResumeWorks/skillgroup/$', SkillGroupListView.as_view(), name='ResumeWorks_skillgroup_list'),
    url(r'^ResumeWorks/skillgroup/create/$', SkillGroupCreateView.as_view(), name='ResumeWorks_skillgroup_create'),
    url(r'^ResumeWorks/skillgroup/detail/(?P<slug>\S+)/$', SkillGroupDetailView.as_view(), name='ResumeWorks_skillgroup_detail'),
    url(r'^ResumeWorks/skillgroup/update/(?P<slug>\S+)/$', SkillGroupUpdateView.as_view(), name='ResumeWorks_skillgroup_update'),
)

urlpatterns += patterns('',
    # urls for Course
    url(r'^ResumeWorks/course/$', CourseListView.as_view(), name='ResumeWorks_course_list'),
    url(r'^ResumeWorks/course/create/$', CourseCreateView.as_view(), name='ResumeWorks_course_create'),
    url(r'^ResumeWorks/course/detail/(?P<slug>\S+)/$', CourseDetailView.as_view(), name='ResumeWorks_course_detail'),
    url(r'^ResumeWorks/course/update/(?P<slug>\S+)/$', CourseUpdateView.as_view(), name='ResumeWorks_course_update'),
)

urlpatterns += patterns('',
    # urls for Reference
    url(r'^ResumeWorks/reference/$', ReferenceListView.as_view(), name='ResumeWorks_reference_list'),
    url(r'^ResumeWorks/reference/create/$', ReferenceCreateView.as_view(), name='ResumeWorks_reference_create'),
    url(r'^ResumeWorks/reference/detail/(?P<slug>\S+)/$', ReferenceDetailView.as_view(), name='ResumeWorks_reference_detail'),
    url(r'^ResumeWorks/reference/update/(?P<slug>\S+)/$', ReferenceUpdateView.as_view(), name='ResumeWorks_reference_update'),
)

urlpatterns += patterns('',
    # urls for Personal
    url(r'^ResumeWorks/personal/$', PersonalListView.as_view(), name='ResumeWorks_personal_list'),
    url(r'^ResumeWorks/personal/create/$', PersonalCreateView.as_view(), name='ResumeWorks_personal_create'),
    url(r'^ResumeWorks/personal/detail/(?P<slug>\S+)/$', PersonalDetailView.as_view(), name='ResumeWorks_personal_detail'),
    url(r'^ResumeWorks/personal/update/(?P<slug>\S+)/$', PersonalUpdateView.as_view(), name='ResumeWorks_personal_update'),
)

urlpatterns += patterns('',
    # urls for ReferenceRequest
    url(r'^ResumeWorks/referencerequest/$', ReferenceRequestListView.as_view(), name='ResumeWorks_referencerequest_list'),
    url(r'^ResumeWorks/referencerequest/create/$', ReferenceRequestCreateView.as_view(), name='ResumeWorks_referencerequest_create'),
    url(r'^ResumeWorks/referencerequest/detail/(?P<slug>\S+)/$', ReferenceRequestDetailView.as_view(), name='ResumeWorks_referencerequest_detail'),
    url(r'^ResumeWorks/referencerequest/update/(?P<slug>\S+)/$', ReferenceRequestUpdateView.as_view(), name='ResumeWorks_referencerequest_update'),
)

urlpatterns += patterns('',
    # urls for Award
    url(r'^ResumeWorks/award/$', AwardListView.as_view(), name='ResumeWorks_award_list'),
    url(r'^ResumeWorks/award/create/$', AwardCreateView.as_view(), name='ResumeWorks_award_create'),
    url(r'^ResumeWorks/award/detail/(?P<slug>\S+)/$', AwardDetailView.as_view(), name='ResumeWorks_award_detail'),
    url(r'^ResumeWorks/award/update/(?P<slug>\S+)/$', AwardUpdateView.as_view(), name='ResumeWorks_award_update'),
)

