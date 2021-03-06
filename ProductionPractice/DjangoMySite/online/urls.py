from django.conf.urls import url

from . import views

app_name = 'online'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^commodity/$', views.commodity, name = 'commodity'),
    url(r'^add_commodity/$', views.add_commodity, name = 'add_commodity'),
    url(r'^logout/$',views.logout,name = 'logout'),
    url(r'^get_user_info/$', views.get_user_info, name = 'get_user_info'),
    url(r'^captcha/$', views.captcha, name = 'captcha'),
]
