# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # docker_image = models.CharField(
        # max_length=100,
        # blank=True,
        # null=True,
        # verbose_name=u"docker容器ID(长)"
    # )

    avatar_link = models.ImageField(
        default="avatar/1.jpg",
        upload_to='avatar',
        verbose_name=u"头像"
    )

    def __unicode__(self):
        return self.user.email


class UserCode(models.Model):
    code_path = models.TextField()
    code_content = models.TextField(
        blank=True,
        null=True
    )

    version = models.IntegerField(
        default=1
    )

    created_time = models.DateTimeField(
        default=timezone.now
    )

    user = models.ForeignKey(User)
    course = models.ForeignKey('courses.Courses')
    lab = models.ForeignKey('labs.Labs')

    def __unicode__(self):
        return self.version

    class Meta:
        get_latest_by = "created_time"
        ordering = ["-created_time"]


class UserDockers(models.Model):
    docker_id = models.CharField(max_length=100)
    docker_open_link = models.URLField()
    docker_type = models.IntegerField(default=0)
    created_time = models.DateTimeField(
        default=timezone.now
    )

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username

    class Meta:
        get_latest_by = "created_time"
        ordering = ["-created_time"]
