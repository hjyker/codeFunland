#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import

import datetime
import logging
from celery import shared_task, task

from django.utils import timezone
from django.contrib.auth.models import User

from labs.utils import (
     docker_init_container_ports, docker_port,
     docker_rm_container,
)
from users.models import UserDockers
from courses.models import Courses
from labs.task_redis import single_one

# docker containers expires time
# It's default 100 hours when development
EXPIRES_HOURS = 2
EXPIRES = datetime.timedelta(hours=EXPIRES_HOURS)

logger = logging.getLogger("views_error")


@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param


@task
def init_docker(user_id, course_id):
    current_user = User.objects.get(id=user_id)

    # Get docker container for current user.
    user_docker = current_user.userdockers_set.first()
    course = Courses.objects.get(id=course_id)

    create_container = False
    if not user_docker:
        create_container = True
    elif timezone.now() - user_docker.created_time >= EXPIRES:
        create_container = True
    else:
        try:
            docker_port(user_docker.docker_id)
        except Exception, ex:
            logger.warning(ex)
            create_container = True

    # create_container = False
    if create_container:
        try:
            new_docker_container = docker_init_container_ports(int(course.label))
            docker_id = new_docker_container.get('Id', None)
            open_link = docker_port(docker_id)

            user_docker = UserDockers.objects.create(
                docker_id=docker_id,
                docker_open_link=open_link,
                user=current_user
            )
        except Exception, ex:
            logger.error(ex)
            user_docker = ex

    return user_docker


@task(name="labs.tasks.rm_periodic_docker")
def rm_periodic_docker():
    # expires = timezone.now() - datetime.timedelta(hours=2)
    expires = timezone.now() - EXPIRES
    user_dockers = UserDockers.objects.filter(
        created_time__lte=expires
    )
    user_dockers_id = user_dockers.values_list(
        "docker_id", flat=True
    )

    if len(user_dockers_id):
        for user_docker in user_dockers:
            rm_container(user_docker)


@single_one(key="rm_one", timeout=10)
def rm_container(user_docker):
    try:
        docker_rm_container(user_docker.docker_id)
    except Exception, ex:
        logger.error(ex)
        user_docker.delete()


