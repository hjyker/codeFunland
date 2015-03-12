#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name='courses_index'),
)
