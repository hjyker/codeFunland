#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import patterns, url
from users import views


urlpatterns = patterns('',
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^profile/(?P<user_id>\d+)/$', views.user_profile, name='user_profile'),
    url(r'^profile/(?P<user_id>\d+)/update/$', views.update_avatar, name='update_avatar'),
    url(r'^change_pwd/$', views.change_pwd, name='change_pwd'),
)
