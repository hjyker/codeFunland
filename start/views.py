# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from courses.models import LearnRecored


def index(request):
    user_recored = None
    if request.user.is_authenticated():
        current_user = request.user
        learn_recored = LearnRecored.objects.filter(
            user=current_user
        ).order_by('-created_time')
        user_recored = learn_recored.first()

    return render(
        request,
        'start/index.html',
        {
            "user_recored": user_recored,
            "nowtime": timezone.now()
        }
    )
