from django.conf.urls import patterns, url, include
from .views import ProjectListView, ExperienceListView, EducationListView, SkillListView, SkillGroupListView, CourseListView, ReferenceListView, PersonalListView, ReferenceRequestListView, AwardListView
from .views import ProjectDetailView, ExperienceDetailView, EducationDetailView, SkillDetailView, SkillGroupDetailView, CourseDetailView, ReferenceDetailView, PersonalDetailView, ReferenceRequestDetailView, AwardDetailView
from .views import ProjectCreateView, ExperienceCreateView, EducationCreateView, SkillCreateView, SkillGroupCreateView, CourseCreateView, ReferenceCreateView, PersonalCreateView, ReferenceRequestCreateView, AwardCreateView
from .views import ProjectUpdateView, ExperienceUpdateView, EducationUpdateView, SkillUpdateView, SkillGroupUpdateView, CourseUpdateView, ReferenceUpdateView, PersonalUpdateView, ReferenceRequestUpdateView, AwardUpdateView

urlpatterns = patterns('')

urlpatterns += patterns('',
    # urls for Project
    url(r'^project/$', ProjectListView.as_view(), name='resume_project_list'),
    url(r'^project/create/$', ProjectCreateView.as_view(), name='resume_project_create'),
    url(r'^project/detail/(?P<slug>\S+)/$', ProjectDetailView.as_view(), name='resume_project_detail'),
    url(r'^project/update/(?P<slug>\S+)/$', ProjectUpdateView.as_view(), name='resume_project_update'),
)

urlpatterns += patterns('',
    # urls for Experience
    url(r'^experience/$', ExperienceListView.as_view(), name='resume_experience_list'),
    url(r'^experience/create/$', ExperienceCreateView.as_view(), name='resume_experience_create'),
    url(r'^experience/detail/(?P<slug>\S+)/$', ExperienceDetailView.as_view(), name='resume_experience_detail'),
    url(r'^experience/update/(?P<slug>\S+)/$', ExperienceUpdateView.as_view(), name='resume_experience_update'),
)

urlpatterns += patterns('',
    # urls for Education
    url(r'^education/$', EducationListView.as_view(), name='resume_education_list'),
    url(r'^education/create/$', EducationCreateView.as_view(), name='resume_education_create'),
    url(r'^education/detail/(?P<slug>\S+)/$', EducationDetailView.as_view(), name='resume_education_detail'),
    url(r'^education/update/(?P<slug>\S+)/$', EducationUpdateView.as_view(), name='resume_education_update'),
)

urlpatterns += patterns('',
    # urls for Skill
    url(r'^skill/$', SkillListView.as_view(), name='resume_skill_list'),
    url(r'^skill/create/$', SkillCreateView.as_view(), name='resume_skill_create'),
    url(r'^skill/detail/(?P<slug>\S+)/$', SkillDetailView.as_view(), name='resume_skill_detail'),
    url(r'^skill/update/(?P<slug>\S+)/$', SkillUpdateView.as_view(), name='resume_skill_update'),
)

urlpatterns += patterns('',
    # urls for SkillGroup
    url(r'^skillgroup/$', SkillGroupListView.as_view(), name='resume_skillgroup_list'),
    url(r'^skillgroup/create/$', SkillGroupCreateView.as_view(), name='resume_skillgroup_create'),
    url(r'^skillgroup/detail/(?P<slug>\S+)/$', SkillGroupDetailView.as_view(), name='resume_skillgroup_detail'),
    url(r'^skillgroup/update/(?P<slug>\S+)/$', SkillGroupUpdateView.as_view(), name='resume_skillgroup_update'),
)

urlpatterns += patterns('',
    # urls for Course
    url(r'^course/$', CourseListView.as_view(), name='resume_course_list'),
    url(r'^course/create/$', CourseCreateView.as_view(), name='resume_course_create'),
    url(r'^course/detail/(?P<slug>\S+)/$', CourseDetailView.as_view(), name='resume_course_detail'),
    url(r'^course/update/(?P<slug>\S+)/$', CourseUpdateView.as_view(), name='resume_course_update'),
)

urlpatterns += patterns('',
    # urls for Reference
    url(r'^reference/$', ReferenceListView.as_view(), name='resume_reference_list'),
    url(r'^reference/create/$', ReferenceCreateView.as_view(), name='resume_reference_create'),
    url(r'^reference/detail/(?P<slug>\S+)/$', ReferenceDetailView.as_view(), name='resume_reference_detail'),
    url(r'^reference/update/(?P<slug>\S+)/$', ReferenceUpdateView.as_view(), name='resume_reference_update'),
)

urlpatterns += patterns('',
    # urls for Personal
    url(r'^personal/$', PersonalListView.as_view(), name='resume_personal_list'),
    url(r'^personal/create/$', PersonalCreateView.as_view(), name='resume_personal_create'),
    url(r'^personal/detail/(?P<slug>\S+)/$', PersonalDetailView.as_view(), name='resume_personal_detail'),
    url(r'^personal/update/(?P<slug>\S+)/$', PersonalUpdateView.as_view(), name='resume_personal_update'),
)

urlpatterns += patterns('',
    # urls for ReferenceRequest
    url(r'^referencerequest/$', ReferenceRequestListView.as_view(), name='resume_referencerequest_list'),
    url(r'^referencerequest/create/$', ReferenceRequestCreateView.as_view(), name='resume_referencerequest_create'),
    url(r'^referencerequest/detail/(?P<slug>\S+)/$', ReferenceRequestDetailView.as_view(), name='resume_referencerequest_detail'),
    url(r'^referencerequest/update/(?P<slug>\S+)/$', ReferenceRequestUpdateView.as_view(), name='resume_referencerequest_update'),
)

urlpatterns += patterns('',
    # urls for Award
    url(r'^award/$', AwardListView.as_view(), name='resume_award_list'),
    url(r'^award/create/$', AwardCreateView.as_view(), name='resume_award_create'),
    url(r'^award/detail/(?P<slug>\S+)/$', AwardDetailView.as_view(), name='resume_award_detail'),
    url(r'^award/update/(?P<slug>\S+)/$', AwardUpdateView.as_view(), name='resume_award_update'),
)

