# -*- coding: utf-8 -*-


from django.contrib import admin

from users.models import (
    UserProfile,
    UserCode
)


class UserCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'lab', 'created_time')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'avatar_link')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserCode, UserCodeAdmin)
