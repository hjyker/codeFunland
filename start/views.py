# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# from django.http import HttpResponse
from django.utils import timezone

from users.forms import (UserRegisterForm, UserLoginForm)


def index(request):
    register_form = UserRegisterForm()
    login_form = UserLoginForm()

    if request.user.is_authenticated():
        return redirect(
            reverse("courses:courses_index", args=[])
        )

    return render(
        request,
        'start/index.html',
        {
            "user_record": False,
            "nowtime": timezone.now(),
            "register_form": register_form,
            "login_form": login_form
        }
    )


def page_not_found(request):
    """
    It's the standard 404 page, when you raise the Http404 exception,
    It's a auto process whole redirect, you just need to write the
    handlerXXX into codeFunland/urls.py
    """
    return render(request, "others/404.html")
