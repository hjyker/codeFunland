# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url
from labs import views

urlpatterns = patterns('',
    url(r'^edit/(?P<course_id>\d+)/(?P<lab_weight>\d+)/$',
        views.edit_code, name="edit_code"),
    url(r"^(?P<course_id>\d+)$", views.show_labs, name="show_labs"),
    url(r'^save_user_code/$',
        views.save_user_code, name="save_user_code"),
)
