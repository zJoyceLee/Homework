from django.conf.urls import url

from . import views

app_name = 'forms'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(),  name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/fill/$', views.fill, name='fill'),
]