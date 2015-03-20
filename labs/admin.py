# -*- coding: utf-8 -*-


from django.contrib import admin

from labs.models import Labs


class LabsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'views',
        'created_time', 'course'
    )


admin.site.register(Labs, LabsAdmin)
