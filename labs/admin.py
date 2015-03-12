# -*- coding: utf-8 -*-


from django.contrib import admin

from labs.models import Labs


class LabsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'docker_image',
        'views', 'document_link', 'created_time', 'course'
    )


admin.site.register(Labs, LabsAdmin)
