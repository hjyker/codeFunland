# -*- coding: utf-8 -*-


from django.db import models
from django.utils import timezone


class Labs(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name=u"实验名称"
    )

    description = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name=u"实验描述"
    )

    # docker_image = models.URLField(
        # max_length=300,
        # blank=True,
        # null=True,
        # verbose_name=u"docker 容器"
    # )

    views = models.IntegerField(
        default=0,
        blank=True,
        verbose_name=u"学习人数"
    )

    # document_link = models.URLField(
        # max_length=300,
        # blank=True,
        # null=True,
        # verbose_name=u"实验文档"
    # )

    created_time = models.DateTimeField(
        default=timezone.now
    )

    # weight: The order in all labs of one course
    weight = models.IntegerField(verbose_name=u"weight")

    course = models.ForeignKey('courses.Courses')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-created_time"]
