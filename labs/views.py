# -*- coding: utf-8 -*-


import datetime
import logging

from django.shortcuts import (render, redirect)
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.http import (HttpResponse, HttpResponseNotFound, Http404)
from django.views.decorators.http import require_http_methods

from users.models import (UserDockers, UserCode)
from courses.models import (LearnRecord, Courses)
from labs.models import Labs
from .utils import (
    docker_ps, docker_init_container_ports, docker_port
)
from labs.forms import UserCodeForm
from courses.constants import COMMAND_PRE

# docker containers expires time
# It's default 100 hours when development
EXPIRES_HOURS = 100
EXPIRES = datetime.timedelta(hours=EXPIRES_HOURS)

logger = logging.getLogger("views_error")


@login_required
def show_labs(request, course_id):
    current_user = request.user
    course_id = int(course_id)
    course = Courses.objects.get(
        id=course_id
    )
    learn_records = course.learnrecord_set.filter(
        user=current_user
    )

    labs_id = [learn_record.lab.id for learn_record in learn_records]
    user_finished_labs = current_user.learnrecord_set.values_list(
        "lab", flat=True
    )

    # Get persent that user finished labs.
    user_finished_labs = len({}.fromkeys(user_finished_labs).keys())
    user_finished_labs_per = user_finished_labs / float(learn_records.count())

    return render(request,
        "labs/show_labs.html",
        {
            "course": course,
            "user_record_latest": learn_records.first(),
            "labs_id": labs_id,
            "user_finished_labs_per": int(user_finished_labs_per * 100),
        }
    )


@login_required
def edit_code(request, course_id, lab_weight):
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
            reverse("courses:courses_index", args=[])
        )

    # It's not accurate that below logic, need rebuild
    if lab_weight > labs.count():
        return redirect(
            reverse("courses:courses_index", args=[])
        )
    ##################################################

    lab = labs.filter(weight=lab_weight).first()

    user_code = current_user.usercode_set.filter(
        lab=lab
    ).first()

    # Get docker container for current user.
    user_docker = current_user.userdockers_set.first()

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

    create_container = False
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

    # docker_info = docker_ps()
    docker_info = False

    return render(
        request,
        "labs/edit_code.html",
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


@require_http_methods(["POST"])
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

            # save learn record for current user
            LearnRecord.objects.create(
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
            logger.error(ex)
            return HttpResponse(error)
        else:
            return HttpResponse(
                reverse(
                    'labs:edit_code',
                    args=[int(course.id), int(lab.weight)+1]
                )
            )
    else:
        return Http404()
