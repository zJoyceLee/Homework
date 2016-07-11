from django.conf.urls import url

from . import views

app_name = 'form'

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$',views.index, name='index'),
    url(r'^info/$', views.info, name='info'),
    url(r'^filling/$', views.filling, name='filling'),
    # url(r'^regist/$',views.regist,name = 'regist'),

    # # url(r'^logout/$',views.logout,name = 'logout'),
    # url(r'^get_user_info/$', views.get_user_info, name = 'get_user_info'),
    # url(r'^captcha/$', views.captcha, name = 'captcha'),
    # url(r'^update_info/$', views.update_info, name = 'update_info'),
]
