#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import

import datetime
import logging
from celery import shared_task, task

from django.utils import timezone
from django.contrib import messages

from labs.utils import (
     docker_init_container_ports, docker_port
)
from users.models import UserDockers

# docker containers expires time
# It's default 100 hours when development
EXPIRES_HOURS = 100
EXPIRES = datetime.timedelta(hours=EXPIRES_HOURS)

logger = logging.getLogger("views_error")


@shared_task
def test(param):
        return 'The test task executed with argument "%s" ' % param


@shared_task
def init_docker(request, user_docker, course):
    current_user = request.user

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
            messages.add_message(request, messages.ERROR, ex)
# end #################################################################
            logger.warning(ex)
            messages.add_message(request,
                messages.WARNING,
                'Your docker container has been not exist, We will Create a New...'
            )
            create_container = True

    # create_container = False
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
            logger.error(ex)
            messages.add_message(request, messages.ERROR, ex)
            user_docker = ex

    return user_docker



