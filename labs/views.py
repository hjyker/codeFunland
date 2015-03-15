# -*- coding: utf-8 -*-


import datetime

from django.shortcuts import (render, redirect)
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.http import (HttpResponse, HttpResponseNotFound)

from users.models import (UserDockers, UserCode)
from courses.models import (LearnRecored, Courses)
from labs.models import Labs
from labs.utils import (
    docker_ps, docker_init_container_ports, docker_port
)
from labs.forms import UserCodeForm
from courses.constants import COMMAND_PRE

# docker containers expires time
# It's default 100 hours when development
EXPIRES_HOURS = 100
EXPIRES = datetime.timedelta(hours=EXPIRES_HOURS)


@login_required
def lab_index(request, course_id, lab_weight):
    course_id = int(course_id)
    lab_weight = int(lab_weight)
    current_user = request.user
    code_form = UserCodeForm()
    course = Courses.objects.get(id=course_id)
    labs = course.labs_set

    # Reback courses.index without labs for this course
    if not labs.exists():
        messages.add_message(request,
            messages.WARNING,
            "Sorry, There is not any lab about this course."
        )
        return redirect(
            reverse("courses.views.index", args=[])
        )

    # It's not accurate that below logic, need rebuild
    if lab_weight > labs.count():
        return redirect(
            reverse("courses.views.index", args=[])
        )
    ##################################################

    lab = labs.filter(weight=lab_weight).first()

    user_code = current_user.usercode_set.filter(
        lab=lab
        ).order_by(
            '-created_time'
        ).first()

    # Get docker container for current user.
    user_docker = current_user.userdockers_set.order_by("-created_time").first()

    # Get docker container's record that currnet user used.
    create_container = False
    if not user_docker:
        create_container = True
    elif timezone.now() - user_docker.created_time >= EXPIRES:
        create_container = True
    else:
        try:
            docker_port(user_docker.docker_id)
        except Exception, ex:
# Test ################################################################
            # messages.add_message(request, messages.ERROR, ex)
# end #################################################################
            messages.add_message(request,
                messages.WARNING,
                'Your docker container has been not exist, We will Create a New...'
            )
            create_container = True

    if create_container:
        try:
            new_docker_container = docker_init_container_ports(int(course.id))
            docker_id = new_docker_container.get('Id', None)
            open_link = docker_port(docker_id)

            user_docker = UserDockers.objects.create(
                docker_id=docker_id,
                docker_open_link=open_link,
                user=current_user
                )
        except Exception, ex:
            messages.add_message(request, messages.ERROR, ex)
            user_docker = ex

    docker_info = docker_ps()

    return render(
        request,
        "labs/lab_index.html",
        {
            "course": course,
            "lab": lab,
            "command_pre": COMMAND_PRE.get(course.label),
            "docker_info": docker_info,
            "user_docker": user_docker,
            "user_code": user_code,
            "code_form": code_form
        }
    )


@login_required
def save_user_code(request):
    if request.method == "POST":
        try:
            error = True
            current_user = request.user
            code_path = request.POST.get('code_path')
            lab_id = int(request.POST.get('lab_id'))
            lab = Labs.objects.filter(id=lab_id).first()
            course = lab.course

            code_content = 'f' + request.POST.get('code_content')
            user_code = current_user.usercode_set.order_by(
                '-created_time'
                ).first()

            # save learn recored for current user
            learn_recored = LearnRecored.objects.create(
                user=current_user,
                course=course,
                lab=lab
            )

            if not user_code:
                version = 1
            else:
                version = int(user_code.version) + 1

            # save code for user
            user_code = UserCode.objects.create(
                code_path=code_path,
                code_content=code_content,
                version=version,
                user=current_user,
                lab=lab,
                course=course
            )
        except Exception, ex:
            error = ex
            return HttpResponse(error)
        else:
            # return redirect(
                # reverse('labs.views.lab_index', args=[int(course.id), lab_id])
            # )
            return HttpResponse(
                reverse(
                    'labs.views.lab_index',
                    args=[int(course.id), int(lab.weight)+1]
                )
            )
    else:
        return HttpResponseNotFound('Wow , woW,<h1>404 NOT FOUND</h1>')
