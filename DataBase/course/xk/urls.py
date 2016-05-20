from django.conf.urls import patterns, url

from xk import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index),

    url(r'^teacher/manage/score/$', views.teacher_manage_score, name='tscore'),
    url(r'^teacher/manage/score/(?P<cno>\w+)$', views.teacher_manage_score, name='tscore/course'),
    url(r'^teacher/manage/course$', views.teacher_manage_course, name='tcourse'),
    url(r'^teacher/manage/student$', views.teacher_manage_student, name='tstudent'),

    url(r'^student/course$', views.student_course, name='scourse'),
    url(r'^student/score$', views.student_score, name='sscore'),

    url(r'^c/new/$', views.c_new, name='cnew'),
    url(r'^c/update/(?P<c_cno>\w+)$', views.c_update, name='cupdate'),
    url(r'^c/delete/(?P<c_cno>\w+)$', views.c_delete, name='cdelete'),

    url(r'^s/new/$', views.s_new, name='snew'),
    url(r'^s/update/(?P<s_sno>\w+)$', views.s_update, name='supdate'),
    url(r'^s/delete/(?P<s_sno>\w+)$', views.s_delete, name='sdelete'),

    url(r'^sc/new_or_delete/$', views.sc_new_or_delete, name='sc/new_or_delete'),
    url(r'^sc/update/(?P<sc_id>\d+)$', views.sc_update, name='scupdate'),

    url(r'^auth$', views.auth, name='auth'),
    url(r'^logout$', views.logout, name='logout')
]
