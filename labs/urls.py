# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url
from labs import views

urlpatterns = patterns('',
    url(r'^index/(?P<course_id>\d+)/(?P<lab_weight>\d+)/$',
        views.lab_index, name="labs_index"),
    url(r'^save_user_code/$',
        views.save_user_code, name="save_user_code"),
)
