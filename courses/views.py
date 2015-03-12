# -*- coding:utf-8 -*-


from django.shortcuts import render

from courses.models import Courses


def index(request):
    courses = Courses.objects.all()
    return render(
        request,
        'courses/courses_index.html',
        {'courses': courses}
    )
