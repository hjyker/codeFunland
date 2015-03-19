# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


class Courses(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
        verbose_name=u"课程名"
    )

    label = models.IntegerField(
        default=0,
        verbose_name=u"课程标签"
    )

    image = models.ImageField(
        default='avatar/1.jpg',
        upload_to='avatar',
        verbose_name=u'课程图片'
    )

    description = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name=u"课程描述"
    )

    created_time = models.DateTimeField(
        default=timezone.now,
        verbose_name=u"创建时间"
    )

    views = models.IntegerField(
        default=0,
        blank=True,
        verbose_name=u"学习人数"
    )

    likes = models.IntegerField(
        default=0,
        blank=True,
        verbose_name=u"关注人数"
    )

    is_active = models.BooleanField(
        default = False,
        verbose_name=u"课程状态"
    )

    owner = models.ForeignKey(
        User,
        related_name='owner'
    )

    users_courses = models.ManyToManyField(
        User,
        through='UsersCourses',
        verbose_name=u'课程完成情况',
        related_name='user_course_related'
    )

    def __unicode__(self):
        return self.name

    # def validate_unique(self, *args, **kwargs):
        # if self.__class__.objects.filter(
                # label=self.label
                # ).exists() and self.label != 0:

            # raise ValidationError(
                # {
                    # NON_FIELD_ERRORS: u"课程标签已存在！"
                # }
            # )


class UsersCourses(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey('Courses')
    is_finished = models.BooleanField(
        default = False,
        verbose_name = u"课程完成状态"
    )

    created_time = models.DateTimeField(
        default=timezone.now
    )


class LearnRecord(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey('Courses')
    lab = models.ForeignKey('labs.Labs')

    created_time = models.DateTimeField(
        default=timezone.now
    )
